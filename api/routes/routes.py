from flask import jsonify, request
from api import app
from api.models.model_load import load_model
from api.models.tratamento_dados import treat_data
import pandas as pd

#endpoint de teste
@app.route('/api/')
def index():
    return "Hello, World!", 200

parameters = ['previous_weight', 'gestational_risk', 'schooling', 'has_hypertension', 'has_diabetes', 'has_pelvic_surgery','has_urinary_infection', 'has_congenital_malformation', 
    'has_family_twinship', 'amount_gestation', 'amount_abortion', 'amount_deliveries','amount_cesarean', 'target', 'age', 'first_prenatal', 'time_between_pregnancies']
#endpoint de predição
@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        #recebe os dados do modelo
        data = request.json
        #lista de parametros do modelo   
        #colocar os parametros na ordem correta para o modelo de acordo com a lista presente em used_columns
        
        # Verificar se os dados recebidos têm as colunas corretas
        if set(data.keys(parameters)) != set():
            return jsonify({'error': 'Invalid columns'}), 400
        
        # Tratar os dados
        treated_data = treat_data(data)
        # Transformar os dados em um DataFrame
        X_test = pd.DataFrame(treated_data, columns=parameters)
        # Carregar o modelo
        model = load_model()
        # predição da classe alvo: 0 ou 1
        y_pred = model.predict(X_test)
        # predição da probabilidade de cada classe: exemplo: [0.1, 0.9]
        y_proba = model.predict_proba(X_test)

        # resultados
        
        result = {
            'prediction': int(y_pred[0]), #predição da classe alvo
            'probability': {
                '0': float(y_proba[0][0]), #predição da probabilidade de ser 0
                '1': float(y_proba[0][1]) #predição da probabilidade de ser 1
            }
        }
        #colocar status
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


    

#endpoint que lista os parâmetros do modelo para o getway
@app.route('/api/parameters', methods=['GET'])
def model_parameters():
    try:
        return jsonify({'message': parameters}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500