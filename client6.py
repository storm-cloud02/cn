import socket
import os #Allows working with the operating system, like checking file sizes or file existence.


def send_file(file_name, server_address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #This line creates a socket (a network communication “door”) that uses IPv4 (AF_INET) and UDP (SOCK_DGRAM), a quick way to send data without needing confirmation for every part..
    file_size = os.path.getsize(file_name) #Gets the total size of the file to keep track of the transfer progress.

    with open(file_name, 'rb') as f: #Opens the file in binary read mode ('rb') to send raw data.
        bytes_sent = 0
        while bytes_sent < file_size: #Runs until all data from the file has been sent (the size of data sent matches the total file size).
            bytes_data = f.read(1024) #Reads 1024 bytes (1 KB) of data at a time from the file. This keeps data pieces small enough to send efficiently without overloading the network.
            if not bytes_data: #If there’s no more data left (the end of the file), it stops the loop.
                break

            sock.sendto(bytes_data, server_address) #Sends each 1024-byte chunk to the specified server.
            bytes_sent += len(bytes_data) #Updates the count of bytes sent and prints out the progress, showing how much of the file has been sent so far.
            print(f"Sending {file_name}: Sent {len(bytes_data)} bytes")

    sock.sendto(b'', server_address)  # End of transmission signal
    print(f"{file_name} sent successfully.")
    sock.close()


def get_file_choice():
    print("Select the type of file you want to send:")
    print("1. Script file (.py)")
    print("2. Text file (.txt)")
    print("3. Audio file (.mp3)")
    print("4. Video file (.mp4)")
    print("5. Other file types")

    choice = input("Enter the number corresponding to your choice: ")
    if choice in ['1', '2', '3', '4', '5']:
        file_type = {
            '1': 'script',
            '2': 'text',
            '3': 'audio',
            '4': 'video',
            '5': 'other'
        }[choice]
        return file_type
    else:
        print("Invalid choice, please try again.")
        return get_file_choice()


if __name__ == "__main__":
    # Set the server IP address and port
    server_address = ('127.0.0.1', 12345)  # Uses 127.0.0.1 (localhost) as the server address; this should be replaced if the server is on a different machine.

    # Choose file type and get file name
    file_type = get_file_choice()
    file_name = input(f"Enter the name of the {file_type} file to send (with extension): ")

    if os.path.isfile(file_name): #Checks if the file exists with os.path.isfile(file_name) before sending.
        send_file(file_name, server_address)
    else:
        print("File does not exist. Please check the file name and try again.")
