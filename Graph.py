import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import socket
import struct

plt.style.use('seaborn')

x_vals = []
y_vals = []

number = 0

HOST = ''
PORT = 1881

socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

socket_object.bind((HOST, PORT))
print('Socket bind complete')


socket_object.listen(10)
print('Socket now listening')

conn, address = socket_object.accept()


def animate(i):
    global number, x_vals, y_vals
    try:
        plt.cla()

        data = conn.recv(8)

        unpacked_data = struct.unpack('f', data)[0]
        unpacked_data = round(unpacked_data, 2)

        y_vals.append(unpacked_data)

        x_vals.append(number)
        number = number + 1

    except:
        pass

    finally:
        plt.plot(x_vals, y_vals)


if __name__ == '__main__':
    try:
        ani = FuncAnimation(plt.gcf(), animate, interval=1)

        plt.tight_layout()
        plt.show()
    except:
        pass

