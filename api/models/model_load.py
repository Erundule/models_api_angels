import pickle
def load_model():
    with open('api/models/modelo_xgboost.pickle', 'rb') as f:
        data = pickle.load(f)

    model = data['modelo']
    #used_columns é só pra confirmar a sequencia certa dos parametros
    used_columns = data['colunas']

    return model, used_columns