from flask import Flask

from gatewayConection import client

app = Flask(__name__)


async def startup():
    await client.start()


async def shutdown():
    await client.stop()


app.on_event("connect", startup)
# app.on_event("disconnect", shutdown())

from api import routes
