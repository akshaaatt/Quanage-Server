from flask import Flask, jsonify, request
from api import run_qasm, get_statevector, get_unitary
import json_tricks

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Hi Qiskitter!"


@app.route('/api/run/qasm', methods=['GET'])
def qasm():
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
    qasm = request.args['qasm']
    backend = request.args['backend']
    print("--------------")
    print('qasm: ', qasm)
    print('backend: ', backend)
    print("^^^^^^^^^^^^^^")
    output = get_unitary(qasm, backend)
    ret_val = json_tricks.dumps(output)  # dump complex vector as json strings
    return ret_val


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
