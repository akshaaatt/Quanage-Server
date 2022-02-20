"""Imports"""
from flask import jsonify, request
import json_tricks
from api import run_qasm, get_statevector, get_unitary


def configure_routes(app):
    """Routes"""
    @app.route('/')
    def welcome():
        """Comments"""
        return "Hi Qiskitter!"

    @app.route('/api/run/qasm', methods=['GET'])
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

    @app.route('/api/run/statevector', methods=['GET'])
    def statevector():
        """Comments"""
        qasm = request.args['qasm']
        backend = request.args['backend']
        print("--------------")
        print('qasm: ', qasm)
        print('backend: ', backend)
        print("^^^^^^^^^^^^^^")
        output = get_statevector(qasm, backend)
        ret_val = json_tricks.dumps(output)  # dump complex vector as json strings
        return ret_val

    @app.route('/api/run/unitary', methods=['GET'])
    def unitary():
        """Comments"""
        qasm = request.args['qasm']
        backend = request.args['backend']
        print("--------------")
        print('qasm: ', qasm)
        print('backend: ', backend)
        print("^^^^^^^^^^^^^^")
        output = get_unitary(qasm, backend)
        ret_val = json_tricks.dumps(output)  # dump complex vector as json strings
        return ret_val