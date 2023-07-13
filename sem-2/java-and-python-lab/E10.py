"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Java and Python Lab.
* Lab Experiment 10 - Implementation of TCP/IP.
"""

# Server.
import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8080)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

print("Server is up and running. Waiting for connections...")

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print("Connected by:", client_address)

    # Receive data from the client
    data = client_socket.recv(1024)
    if data:
        print("Received data:", data.decode())

        # Send a response back to the client
        response = f"Right back at ya client {data.decode()[-2]}!"
        client_socket.sendall(response.encode())

    # Close the connection
    client_socket.close()
