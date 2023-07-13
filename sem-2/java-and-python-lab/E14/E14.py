"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Java and Python Lab.
* Lab Experiment 14 - Build a concurrent multithreaded file transfer server using threads 
"""

import socket
import threading
import os

def handle_client(connection):
    try:
        # Receive the filename from the client
        filename = connection.recv(1024).decode()

        # Check if the file exists
        if os.path.isfile(filename):
            # Open the file and read its contents
            with open(filename, 'rb') as file:
                data = file.read()

            # Send the file contents to the client
            connection.send(data)
        else:
            # Send an error message to the client
            connection.send("File not found".encode())
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

def start_server(host, port):
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)

    print(f"Server started on {host}:{port}")

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()

        print(f"Client connected: {addr}")

        # Create a new thread to handle the client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

# Start the server
start_server('localhost', 8080)
