"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Java and Python Lab.
* Lab Experiment 15 - Implementation of concurrent chat server that allows current logged in users to communicate one with other.
"""

import socket
import threading


class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.connections = []
        self.nicknames = []

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"New connection from {client_address}")
            client_thread = threading.Thread(
                target=self.handle_client, args=(client_socket,)
            )
            client_thread.start()

    def broadcast(self, message):
        for connection in self.connections:
            connection.send(message)

    def handle_client(self, client_socket):
        nickname = client_socket.recv(1024).decode()
        self.nicknames.append(nickname)
        self.connections.append(client_socket)

        self.broadcast(f"{nickname} has joined the chat!\n".encode())

        while True:
            try:
                message = client_socket.recv(1024)
                self.broadcast(f"{nickname}: {message.decode()}".encode())
            except ConnectionResetError:
                index = self.connections.index(client_socket)
                self.connections.remove(client_socket)
                self.nicknames.remove(nickname)
                self.broadcast(f"{nickname} has left the chat.\n".encode())
                client_socket.close()
                break


if __name__ == "__main__":
    server = ChatServer("localhost", 10000)
    server.start()
