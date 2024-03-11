from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from api.models.prediction_model import predict_test
from api.models.data_validation import data_validation
from api.models.data_treatment import data_treatment

api_blueprint = Blueprint('api', __name__)

# Configurar a chave secreta para assinar os tokens JWT
api_blueprint.config = {}
api_blueprint.config['JWT_SECRET_KEY'] = 'secreto'
api_blueprint.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)  # Token expira em 1 dia

# Simulação de banco de dados de usuários
users = {
    'usuario1': 'senha1',
    'usuario2': 'senha2'
}

# Endpoint de login para obter o token JWT
@api_blueprint.route('/api/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"mensagem": "Solicitação JSON inválida"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username not in users or users[username] != password:
        return jsonify({"mensagem": "Credenciais inválidas"}), 401

    # Gerar token JWT
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


# Endpoint de teste
@api_blueprint.route('/api/')
@jwt_required()  # Autenticação JWT necessária
def index():
    return "Hello, World!", 200

# Lista de parâmetros do modelo
parameters = ['previous_weight', 'gestational_risk', 'schooling', 'has_hypertension', 'has_diabetes', 'has_pelvic_surgery','has_urinary_infection', 'has_congenital_malformation', 
    'has_family_twinship', 'amount_gestation', 'amount_abortion', 'amount_deliveries','amount_cesarean', 'mothers_birth_date', 'date_start_pregnancy', 'date_first_prenatal', 'date_last_delivery']

# Endpoint de predição
@api_blueprint.route('/api/predict', methods=['POST'])
@jwt_required()  # Autenticação JWT necessária
def predict():
    try:
        #recebe os dados do modelo
        data = request.json
        #colocar os parametros na ordem correta para o modelo de acordo com a lista presente em used_columns
        
        # Validar os dados
        data_is_invalid = data_validation(data) is not True
        if data_is_invalid:
            validation_error_number = data_validation(data)
            result = {'error_number':validation_error_number}
            return result, 422
        
        # Tratar os dados
        treated_data = data_treatment(data)
        # Transformar os dados em um DataFrame
        X_test = [treated_data]
        print(X_test)
        # Carregar o modelo
        prediction = predict_test(X_test)
        # Retornar a predição
        return jsonify(prediction), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint que lista os parâmetros do modelo para o getway
@api_blueprint.route('/api/parameters', methods=['GET'])
@jwt_required()  # Autenticação JWT necessária
def model_parameters():
    try:
        return parameters, 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
