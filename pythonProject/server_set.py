import socket
import random

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 12345  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    data = conn.recv(1024).decode()
    decd = [ord(c) for c in set(data)]
    rand = get_random(1, 100, 25)
    common = list(set(decd).intersection(rand))
    conn.send(bytes(common))
    common.sort()
    print(common)
    conn.send(bytes(common))
    print("End of the server")

    # while True:
    #     # receive data stream. it won't accept data packet greater than 1024 bytes
    #     data = conn.recv(1024).decode()
    #     print(type(data))
    #     decd = [ord(c) for c in set(data)]
    #     rand = get_random(1, 100, 25)
    #     common = list(set(decd).intersection(rand))
    #     conn.send(bytes(common))
    #     if not data:
    #         # if data is not received break
    #         break
    #     print("from connected user: ", decd)
    #     data = input(' -> ')
    #     conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


def get_random(initial, final, number):
    sample_values = random.sample(range(initial, final), number)
    return sample_values


if __name__ == '__main__':
    server_program()
