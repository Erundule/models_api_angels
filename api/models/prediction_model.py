import pickle

def predict_test(X_test):
    with open('modeltest\modelo_xgboost.pickle', 'rb') as f:
        data = pickle.load(f)

    modelo = data['modelo']

    y_pred = modelo.predict(X_test)
    y_proba = modelo.predict_proba(X_test)
    
    print(y_pred[0])
    print(y_proba[0][0])
    print(y_proba[0][1])