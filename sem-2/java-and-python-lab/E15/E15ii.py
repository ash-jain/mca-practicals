    import socket
    import threading

    class ChatClient:
        def __init__(self, host, port):
            self.host = host
            self.port = port
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        def connect(self):
            self.client_socket.connect((self.host, self.port))
            nickname = input("Enter your nickname: ")
            self.client_socket.send(nickname.encode())
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()

            while True:
                message = input()
                self.client_socket.send(message.encode())

        def receive_messages(self):
            while True:
                try:
                    message = self.client_socket.recv(1024).decode()
                    print(message)
                except ConnectionResetError:
                    print("Disconnected from the server.")
                    self.client_socket.close()
                    break


    if __name__ == '__main__':
        client = ChatClient('localhost', 10000)
        client.connect()
