import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('localhost', 9999))

# Send message to server
client_socket.send("Hello from client!".encode())

# Receive server reply
reply = client_socket.recv(1024).decode()
print("Server replied:", reply)

# Close connection
client_socket.close()
