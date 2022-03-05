"""Import Qiskit"""
from qiskit import QuantumCircuit, BasicAer, execute


def run_qasm(qasm, backend_to_run='qasm_simulator', num_shots_str='1'):
    circuit = QuantumCircuit.from_qasm_str(qasm)
    backend = BasicAer.get_backend(backend_to_run)
    job_sim = execute(circuit, backend, shots=int(num_shots_str))
    result_sim = job_sim.result()
    return result_sim.get_counts(circuit)
