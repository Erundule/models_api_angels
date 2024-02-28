import pickle

with open('modelo_xgboost.pickle', 'rb') as f:
    data = pickle.load(f)

modelo = data['modelo']

X_test = [[60.8, 1, 3, 0, 1, 0, 1, 0, 1, 4, 1, 2, 3, 24, 32, -1]]
# predição da classe alvo: 0 ou 1 y_pred = modelo.predict(X_test)
# predição da probabilidade de cada classe: exemplo: [0.1, 0.9]
y_proba = modelo.predict_proba(X_test)