import pickle
with open('modelo_xgboost.pickle', 'rb') as f:
    data = pickle.load(f)

model = data['modelo']
used_columns = data['colunas']