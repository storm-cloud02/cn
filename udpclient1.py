import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 9090)

message = 'Hello, UDP Server!'
print('Sending:', message)
client_socket.sendto(message.encode(), server_address)

client_socket.close()