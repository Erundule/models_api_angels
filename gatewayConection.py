from py_eureka_client.eureka_client import EurekaClient

eureka_server = 'http://localhost:'
app_name = 'modelo-api-angels'
instance_host = 'localhost'
instance_port = 8000

client = EurekaClient(eureka_server=eureka_server, app_name=app_name,
                      instance_host=instance_host, instance_port=instance_port,
                      status_page_url="/docs")