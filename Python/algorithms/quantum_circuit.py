from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator  # Importar AerSimulator
from qiskit.visualization import plot_histogram

# Crear un circuito cuántico con 1 qubit y 1 bit clásico
circuit = QuantumCircuit(1, 1)

# Aplicar la puerta Hadamard
circuit.h(0)

# Medir el qubit y almacenar el resultado en el bit clásico
circuit.measure(0, 0)

# Mostrar el circuito
print(circuit)

# Usar AerSimulator
simulator = AerSimulator()  # Crear una instancia de AerSimulator

# Ejecutar el circuito
job = simulator.run(circuit, shots=1024)  # Ejecutar el circuito con el simulator
result = job.result()

# Obtener y mostrar los resultados
counts = result.get_counts(circuit)
print("Resultados de la medición:", counts)

# Opcional: Mostrar un histograma de los resultados
#plot_histogram(counts).show()

