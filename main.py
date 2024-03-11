from api import app
from py_eureka_client import eureka_client
from flask_jwt_extended import JWTManager

# Parametros para o eureka
eureka_server = '-'
app_name = 'modelo-api-angels'
instance_host = '0.0.0.0'
instance_port = 5000

# Inicializando o Eureka
eureka_client.init(eureka_server=eureka_server, app_name=app_name,
                  instance_host=instance_host, instance_port=instance_port,
                  status_page_url="/api/")


# Configurar a chave secreta para assinar os tokens JWT
app.config['JWT_SECRET_KEY'] = 'secreto'

jwt = JWTManager(app)

# Registrar o blueprint da API
from api.routes.routes import api_blueprint
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
