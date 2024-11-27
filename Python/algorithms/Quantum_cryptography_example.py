import bases
import bits
from qiskit import QuantumCircuit, Aer, execute
import random

from scipy.ndimage import measurements


# Generate qubits with random gates for Alice and Bob
def bb84_protocol():
    circuit = QuantumCircuit(1, 1)
    bases_alice = [random.choice(['Z', 'X']) for _ in range(10)]
    bits_alice = [random.randint(0, 1) for _ in range(10)]
    measurements = []

    for base, bit in zip(bases_alice, bits_alice):
        if bit == 1:
            circuit.x(0)
        if base == 'X':
            circuit.h(0)
        circuit.measure(0, 0)

        # Execute in simulator
        #simulator = Aer.get_backend('qasm_simulator')
        #result = execute(circuit, simulator, shots=1).result()
        #measurement = int(list(result.get_counts())[0], 2)
        #measurements.append(measurement)

    #return bases_alice, bits_alice, measurements


# Run the protocol
bb84_protocol()
print("Alice's Bases:", bases)
print("Alice's Bits:", bits)
print("Measurement Results:", measurements)
