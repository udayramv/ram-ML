import random
import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)

    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        print(data)
        data = data.split(" ")
        # if 'hello' in data or 'Hello' in data:
        #     if 'Client' in data or 'client' in data:
        #         ind = data.index('Client')
        #         st = "Hello " + data[ind] + ", Glad to meet you"
        #         st = input(" -> ")
        #         conn.send(st.encode())
        #         break
        #     else:
        #         st = input(" -> ")
        #         conn.send(st.encode())
        #         # conn.send("Hello, Glad to meet you".encode())
        #         break
        # elif 'search' in data or 'Search' in data:
        #     if '?' in data:
        #         st = input(" -> ")
        #         conn.send(st.encode())
        #         # conn.send("Sure please hold on".encode())
        #         reply_data = conn.recv(1024).decode()
        #         print(reply_data)
        #         st = input(" -> ")
        #         conn.send(st.encode())
        #         # conn.send("Found few results, Take a look at the following".encode())
        #         break
        #     elif None in data:
        #         st = input(" -> ")
        #         conn.send(st.encode())
        #         break
        #         # conn.send("Nada, didn't find any file that matches your query string".encode())
        #     else:
        #         st = input(" -> ")
        #         conn.send(st.encode())
        #         break
        #         # conn.send("Query string too long, what are you trying to do?".encode())
        if 'exit' in data:
            conn.send('exit'.encode())
            break
        else:
            st = input(" -> ")
            conn.send(st.encode())
            # conn.send("Huh, I didn't understand that, please rephrase and ask again".encode())


    # while True:
    #     # receive data stream. it won't accept data packet greater than 1024 bytes
    #     data = conn.recv(1024).decode()
    #     if not data:
    #         # if data is not received break
    #         break
    #     print("from connected user: " + str(data))
    #     data = input(' -> ')
    #     conn.send(data.encode())  # send data to the client

    conn.close()


if __name__ == '__main__':
    server_program()
