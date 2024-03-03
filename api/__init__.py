from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

from models_api_angels.api.routes import routes