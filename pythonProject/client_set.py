import socket
import random

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    # port = 5000  # socket server port number
    ports = 12345  # server port
    portc = 32451

    client_socket = socket.socket()  # instantiate
    client_socket.bind((host, portc))
    client_socket.connect((host, ports))  # connect to the server

    message = input(" -> ")  # take input
    sample_values = random.sample(range(1, 100), 25)
    client_socket.send(bytes(sample_values))
    data = client_socket.recv(1024).decode()
    common_data = [ord(c) for c in set(data)]
    print("common elements", common_data)
    data_sort = client_socket.recv(1024).decode()
    common_data_sorted = [ord(c) for c in set(data_sort)]
    common_data_sorted.sort()
    print("common elements sorted", common_data_sorted)
    print("Printed the sorted common elements")

    client_socket.close()  # close the connection


def get_random(initial, final, number):
    sample_values = random.sample(range(initial, final), number)
    return sample_values


if __name__ == '__main__':
    client_program()