"""Imports"""
from flask import jsonify, request
from api import run_qasm


def configure_routes(app):
    """Routes"""
    @app.route('/')
    def welcome():
        """Comments"""
        return "Hi Qiskitter!"

    @app.route('/api/entangle', methods=['GET', 'POST'])
    def qasm_():
        """Comments"""
        qasm = request.args['qasm']
        backend = request.args['backend']
        num_shots = request.args['num_shots']
        print("--------------")
        print('qasm: ', qasm)
        print('backend: ', backend)
        print('num_shots: ', num_shots)
        print("^^^^^^^^^^^^^^")
        output = run_qasm(qasm, backend, num_shots)
        ret = {"result": output}
        return jsonify(ret)
