import socket
import struct
import time
import random

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 1881))

time_step = [0]

start_time = time.time()

while True:
    instant_time = time.time()

    time_difference = int(instant_time - start_time)

    rand_number = random.uniform(0.1, 1.5)

    rand_number = round(rand_number, 2)

    byte_data = struct.pack('f', rand_number)

    if time_difference > time_step[0]:
        client_socket.send(byte_data)

    time_step[0] = time_difference



