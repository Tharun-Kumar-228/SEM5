import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind IP and Port
server_socket.bind(('localhost', 9999))

# Listen for incoming connections
server_socket.listen(1)
print("Server listening on port 9999...")

# Accept client connection
conn, addr = server_socket.accept()
print(f"Connected to {addr}")

# Receive message from client
data = conn.recv(1024).decode()
print("Client says:", data)

# Send reply to client
conn.send("Message received!".encode())

# Close connection
conn.close()
server_socket.close()
