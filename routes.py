"""Imports"""
from flask import jsonify
import qrng


def configure_routes(app):
    """Routes"""

    @app.route('/')
    def welcome():
        """Welcome Users"""
        return "Hi Qiskitter!"

    @app.route('/api/key', methods=['GET', 'POST'])
    def qrng_key():
        """Comments"""
        qrng.set_backend('ibmq_mumbai')
        return jsonify(qrng.get_random_int64())
