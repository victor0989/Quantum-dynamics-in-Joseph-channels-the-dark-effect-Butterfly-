import matplotlib.pyplot as plt
import numpy as np

# Configuration parameters
CLK_FREQ = 50000000  # Clock frequency (50 MHz)
BAUD_RATE = 9600     # Baud rate
BIT_PERIOD = CLK_FREQ / BAUD_RATE  # Bit period
DATA_BITS = 8        # Number of data bits

def transmit_rs232(tx_data, start_tx):
    if start_tx:
        # Add start bit (0), data, and stop bit (1)
        tx_shift = [0] + tx_data + [1]
        tx_signal = []
        for bit in tx_shift:
            tx_signal.extend([bit] * int(BIT_PERIOD))  # Expand each bit according to the period
        return tx_signal
    else:
        return []

# Example data to transmit (8 bits)
data_to_send = [1, 0, 1, 1, 0, 1, 0, 1]  # Example: 0b10110101
start_tx = True  # Indicates that transmission is starting

# Generate the transmission signal
tx_signal = transmit_rs232(data_to_send, start_tx)

# Create time for the signal
time = np.arange(len(tx_signal)) / CLK_FREQ

# Plot the transmission signal
plt.figure(figsize=(10, 4))
plt.step(time, tx_signal, where='post')
plt.title('RS232 Transmission Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage Level (0 or 1)')
plt.ylim(-0.1, 1.1)
plt.grid()
plt.show()
