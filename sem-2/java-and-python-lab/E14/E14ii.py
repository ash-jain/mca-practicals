import socket

def start_client(host, port):
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))

        # Request a file name from the user
        filename = input("Enter the file name: ")

        # Send the file name to the server
        client_socket.send(filename.encode())

        # Receive the file contents from the server
        data = client_socket.recv(1024)

        # Check if the file exists
        if data.decode() == "File not found":
            print("File not found on the server.")
        else:
            # Save the received file contents to a new file
            with open(filename, 'wb') as file:
                file.write(data)

            print(f"File '{filename}' downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()

# Start the client
start_client('localhost', 8080)
