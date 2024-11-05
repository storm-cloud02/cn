import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
server_socket.bind(server_address)
server_socket.listen(1)

print('TCP Server is listening on {}:{}'.format(*server_address))

while True:
    print('Waiting for a connection...')
    connection, client_address = server_socket.accept()

    print('Connection from', client_address)

    data = connection.recv(1024)
    while data:
        print('Received:', data.decode())
        data = connection.recv(1024)

    connection.close()