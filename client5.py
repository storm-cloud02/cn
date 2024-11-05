#The Socket library in Python is a tool that lets programs talk to each other over a network, like the internet or a local network.
#A socket is like a phone line; it connects two devices so they can send and receive data back and forth.
#Using the socket library, you can create programs that act as a server (like a website or a game server) and others that act as clients (like your web browser or game client).

import socket

def client_program():
    host = socket.gethostname()  #  This gets the local machine's name, assuming the server is on the same device.
    port = 5000  # socket server port number

    client_socket = socket.socket()  #  This creates a socket object to handle network communication.
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  #  # asks user for input message

    while message.lower().strip() != 'bye': # keeps running unless 'bye' is typed
        client_socket.send(message.encode())  #  Sends the user’s message to the server.
        data = client_socket.recv(1024).decode()  # receives the server’s response (up to 1024 bytes)

        print('Received from server: ' + data) # prints the server’s response

        message = input(" -> ") # prompts the user for a new message

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()











