from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Configurar a chave secreta para assinar os tokens JWT
app.config['JWT_SECRET_KEY'] = 'secreto'

jwt = JWTManager(app)

# Registrar o blueprint da API
from api.routes.routes import api_blueprint
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
