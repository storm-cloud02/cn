import socket


# Function to resolve URL to IP address
'''
Purpose: Converts a given URL (like www.example.com) into its corresponding IP address (like 192.0.2.1).
How It Works:
It uses the socket.gethostbyname(url) function to look up the IP address.
If successful, it returns a message with the IP address.
If the URL cannot be resolved (like a typo in the URL), it catches the error and returns a message saying it was unable to resolve the URL.
'''
def url_to_ip(url):
    try:
        ip_address = socket.gethostbyname(url)
        return f"The IP address of {url} is: {ip_address}"
    except socket.gaierror:
        return f"Unable to resolve {url}"


# Function to resolve IP address to URL
'''
Purpose: Converts a given IP address back into its corresponding URL.
How It Works:
It uses socket.gethostbyaddr(ip) to find the URL associated with the given IP address.
If successful, it returns a message with the URL.
If the IP address cannot be resolved (maybe it's not associated with a hostname), it catches the error and returns a message indicating the failure.
'''
def ip_to_url(ip):
    try:
        url = socket.gethostbyaddr(ip)
        return f"The URL for IP address {ip} is: {url[0]}"
    except socket.herror:
        return f"Unable to resolve {ip}"


# Main function to take input and call the respective function
def main():
    print("DNS Lookup Tool")
    print("1. Lookup URL to IP")
    print("2. Lookup IP to URL")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        url = input("Enter the URL (without http/https): ")
        print(url_to_ip(url))
    elif choice == '2':
        ip = input("Enter the IP address: ")
        print(ip_to_url(ip))
    else:
        print("Invalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()

