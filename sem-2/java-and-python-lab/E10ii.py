import socket
import sys

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 8080)
client_socket.connect(server_address)

# Send data to the server
message = f"Hello, server from client {sys.argv[1]}!"
client_socket.sendall(message.encode())

# Receive a response from the server
response = client_socket.recv(1024)
print("Received response:", response.decode())

# Close the connection
client_socket.close()
