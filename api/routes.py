from api import app
from flask import request

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    return "Predict"

@app.route('/parameters', methods=['GET'])
def model_parameters():
    parameters = ['previous_weight', 'gestational_risk', 'schooling', 'has_hypertension', 'has_diabetes', 'has_pelvic_surgery','has_urinary_infection', 'has_congenital_malformation', 
    'has_family_twinship', 'amount_gestation', 'amount_abortion', 'amount_deliveries','amount_cesarean', 'target', 'age', 'first_prenatal', 'time_between_pregnancies']   
    return parameters