from api import app
# from gatewayConection import client

# async def startup():
#     await client.start()


# async def shutdown():
#     await client.stop()

# app.on_event("connect", startup)
# # app.on_event("disconnect", shutdown())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    