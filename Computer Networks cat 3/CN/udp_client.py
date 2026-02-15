import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ('localhost', 9999)

# Send message
client_socket.sendto("Hello UDP Server!".encode(), server_address)

# Receive reply
data, _ = client_socket.recvfrom(1024)
print("Server replied:", data.decode())

# Close socket
client_socket.close()
