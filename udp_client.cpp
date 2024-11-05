#include <iostream>
#include <cstring>
#include <arpa/inet.h>
#include <unistd.h>

#define PORT 8080

int main() {
    int sock;
    struct sockaddr_in serv_addr;
    const char* message = "Hello from UDP Client";
    char buffer[1024] = {0};
    socklen_t addr_len = sizeof(serv_addr);

    // Creating socket file descriptor
    if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&serv_addr, 0, sizeof(serv_addr));

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
    serv_addr.sin_addr.s_addr = INADDR_ANY;

    sendto(sock, message, strlen(message), MSG_CONFIRM, (const struct sockaddr*)&serv_addr, addr_len);
    std::cout << "Message sent from client\n";

    int n = recvfrom(sock, (char*)buffer, 1024, MSG_WAITALL, (struct sockaddr*)&serv_addr, &addr_len);
    buffer[n] = '\0';
    std::cout << "Message from server: " << buffer << std::endl;

    close(sock);
    return 0;
}
