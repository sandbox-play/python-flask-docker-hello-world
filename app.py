from flask import Flask
from elasticapm.contrib.flask import ElasticAPM
import os

app = Flask(__name__)

server_url = 'http://apm-server.logging:8200'
service_name = 'DemoFlask'
environment = 'dev'

apm = ElasticAPM(app, server_url=server_url, service_name=service_name, environment=environment)
@app.route("/")
def hello():
    return "Flask inside Docker!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
