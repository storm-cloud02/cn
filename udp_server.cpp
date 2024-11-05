#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

#define PORT 8080

int main() {
    int server_fd;
    struct sockaddr_in address, client_addr;
    char buffer[1024] = {0};
    const char* response = "Hello from UDP Server";
    socklen_t addr_len = sizeof(client_addr);

    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&address, 0, sizeof(address));
    memset(&client_addr, 0, sizeof(client_addr));

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Binding the socket with the server address
    if (bind(server_fd, (const struct sockaddr*)&address, sizeof(address)) < 0) {
        perror("Bind failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    int n = recvfrom(server_fd, (char*)buffer, 1024, MSG_WAITALL, (struct sockaddr*)&client_addr, &addr_len);
    buffer[n] = '\0';
    std::cout << "Message from client: " << buffer << std::endl;

    sendto(server_fd, response, strlen(response), MSG_CONFIRM, (const struct sockaddr*)&client_addr, addr_len);
    std::cout << "Response sent from server\n";

    close(server_fd);
    return 0;
}
