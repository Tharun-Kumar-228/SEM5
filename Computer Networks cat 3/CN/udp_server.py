import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind IP and Port
server_socket.bind(('localhost', 9999))
print("UDP Server listening on port 9999...")

while True:
    # Receive data from client
    data, addr = server_socket.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")

    # Send reply to client
    server_socket.sendto("Hello from UDP server!".encode(), addr)
