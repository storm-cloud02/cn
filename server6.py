import socket


def receive_file(save_path, listen_address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(listen_address)

    with open(save_path, 'wb') as f: #Opens a new file in binary write mode ('wb') to save incoming raw data.
        print("Waiting to receive file...")
        while True:
            data, addr = sock.recvfrom(1024) #Receives up to 1024 bytes at a time from the client.
            if not data:  # Check for end-of-transmission signal
                print("File received successfully.")
                break
            f.write(data)
            print(f"Receiving: Received {len(data)} bytes from {addr}")

    sock.close()


if __name__ == "__main__":
    # Listen on all available interfaces on port 12345
    listen_address = ('0.0.0.0', 12345) #When you bind a socket to 0.0.0.0, it tells the server to listen for incoming connections on all available network interfaces (or IP addresses) of the machine. This means that the server can accept connections not only from the local host (localhost) but also from any other machines in the network.
    save_path = "received_file.py"  # You can change this to save with different file names
    receive_file(save_path, listen_address)


#
