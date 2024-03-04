from flask import Flask
from flask_cors import CORS


from gatewayConection import client

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

async def startup():
    await client.start()


async def shutdown():
    await client.stop()


app.on_event("connect", startup)
# app.on_event("disconnect", shutdown())

from models_api_angels.api.routes import routes