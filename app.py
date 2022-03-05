"""Imports"""
from flasgger import Swagger
from flask import Flask

from routes import configure_routes

app = Flask(__name__)
swagger = Swagger(app)
configure_routes(app)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
