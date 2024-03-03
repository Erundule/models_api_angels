from flask import jsonify
from api import app

#endpoint de teste
@app.route('/api/')
def index():
    return "Hello, World!", 200

#endpoint de predição
@app.route('/api/predict', methods=['POST'])
def predict():
    return "predict", 200


#endpoint que lista os parâmetros do modelo para o getway
@app.route('/api/parameters', methods=['GET'])
def model_parameters():
    parameters = ['previous_weight', 'gestational_risk', 'schooling', 'has_hypertension', 'has_diabetes', 'has_pelvic_surgery','has_urinary_infection', 'has_congenital_malformation', 
    'has_family_twinship', 'amount_gestation', 'amount_abortion', 'amount_deliveries','amount_cesarean', 'target', 'age', 'first_prenatal', 'time_between_pregnancies']   
    return jsonify({'message': parameters}), 200