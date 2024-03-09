from py_eureka_client import eureka_client

eureka_server = 'http://localhost:'
app_name = 'modelo-api-angels'
instance_host = 'localhost'
instance_port = 5000

eureka_client.init(eureka_server=eureka_server, app_name=app_name,
                  instance_host=instance_host, instance_port=instance_port,
                  status_page_url="/docs")