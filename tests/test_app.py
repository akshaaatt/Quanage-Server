"""Imports"""
from flask import Flask
from routes import configure_routes


def test_base_route():
    """Comments"""
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hi Qiskitter!'
    assert response.status_code == 200
