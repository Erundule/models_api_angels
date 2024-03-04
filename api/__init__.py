from flask import Flask

from gatewayConection import client

app = Flask(__name__)

@app.on_event("startup")
async def startup():
    await client.start()

@app.on_event("shutdown")
async def shutdown():
    await client.stop()

from api import routes