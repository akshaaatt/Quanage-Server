"""Imports"""
from flask import jsonify, request
from api import run_qasm
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
        qrng.set_provider_as_IBMQ('57fcd139a2ca2e77337f1f5dc2a5a39a2aa0c862981fcb33a2469bc63f47a22a3c8df9f074157f984ee96896ffeb3886f44a137a0b967922f05b91b4ae494a6b')
        qrng.set_backend('ibmq_mumbai')
        return jsonify(qrng.get_random_int64())
