import socket
import random

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # client_socketect to the server

    # data = client_socket.recv(1024).decode()
    while True:
        data = client_socket.recv(1024).decode()
        print("Recieved -> ", data)
        if 'exit' in data:
            break
        # if 'hello' in message or 'Hello' in message:
        #     if 'Client' in message or 'client' in message:
        #         ind = message.index('Client')
        #         # st = "Hello " + message[ind] + ", Glad to meet you"
        #         # print(st)
        #         data = client_socket.recv(1024).decode()
        #         print("Recieved -> ", data)
        #         break
        #     else:
        #         data = client_socket.recv(1024).decode()
        #         print("Recieved ", data)
        #         break
        # elif 'search' in message or 'Search' in message:
        #         if '?' in message:
        #             data = client_socket.recv(1024).decode()
        #             print("Recieved ", data)
        #             st = input(" -> ")
        #             client_socket.send(st.encode())
        #             # client_socket.send("No problem, take your time".encode())
        #             data = client_socket.recv(1024).decode()
        #             print("Recieved ", data)
        #             break
        #         elif 'None' in message:
        #             data = client_socket.recv(1024).decode()
        #             print("Recieved ", data)
        #             break
        #         else:
        #             data = client_socket.recv(1024).decode()
        #             print("Recieved ", data)
        #             break
        # else:
        #         data = client_socket.recv(1024).decode()
        #         print("Recieved -> ", data)

        else:
            data = client_socket.recv(1024).decode()
            print("Recieved -> ", data)


    client_socket.close() # close the client_socketection


if __name__ == '__main__':
    client_program()