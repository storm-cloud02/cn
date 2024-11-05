import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 9090)
server_socket.bind(server_address)

print('UDP Server is listening on {}:{}'.format(*server_address))

while True:
    print('Waiting for a message...')
    data, client_address = server_socket.recvfrom(1024)

    print('Received:', data.decode(), 'from', client_address)
