"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Java and Python Lab.
* Lab Experiment 13 - Implementation of File access using RPC in python.
"""


import Pyro4

@Pyro4.expose
class FileServer:
    def read_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return "File not found."

    def write_file(self, file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            return "File written successfully."
        except Exception as e:
            return str(e)


# Set up Pyro4 daemon and register the file server object
daemon = Pyro4.Daemon()
uri = daemon.register(FileServer)

# Print the URI for the client to use
print("File Server URI:", uri)

# Start the server and wait for requests
daemon.requestLoop()
