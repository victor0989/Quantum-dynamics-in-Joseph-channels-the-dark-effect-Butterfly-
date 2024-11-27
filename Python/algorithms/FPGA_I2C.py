import time

# Define initial state of the signals
sda = 1   # Data line
scl = 1   # Clock line

def start_condition():
    global sda, scl
    sda = 1
    scl = 1
    print("Starting START condition")
    sda = 0
    print("SDA goes low", "SDA:", sda, "SCL:", scl)

def stop_condition():
    global sda, scl
    sda = 0
    scl = 1
    print("Starting STOP condition")
    sda = 1
    print("SDA goes high", "SDA:", sda, "SCL:", scl)

def clock_pulse():
    global scl
    scl = 0
    print("SCL goes low", "SDA:", sda, "SCL:", scl)
    time.sleep(0.5)
    scl = 1
    print("SCL goes high", "SDA:", sda, "SCL:", scl)
    time.sleep(0.5)

def send_bit(bit):
    global sda
    sda = bit
    print("Sending bit:", bit, "SDA:", sda, "SCL:", scl)
    clock_pulse()

# Sequence example
start_condition()
send_bit(1)
send_bit(0)
send_bit(1)
send_bit(1)
stop_condition()

