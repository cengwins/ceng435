# echo-client.py

import socket
HOST = socket.gethostbyname("server")  # Use this if you are using docker compose
# if you do not use docker compose, instead of resolving name
# set host to the ip address directly
#HOST = "172.19.0.2"
PORT = 8000  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((HOST, PORT))  # connect to the server

message = input(" -> ")  # take input

while message.lower().strip() != 'bye':
    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response

    print('Received from server: ' + data)  # show in terminal

    message = input(" -> ")  # again take input

client_socket.close()  # close the connection