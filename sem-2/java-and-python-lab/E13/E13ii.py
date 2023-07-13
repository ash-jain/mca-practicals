import Pyro4

# Get the file server object using the server URI
server_uri = input("Enter the File Server URI: ")
file_server = Pyro4.Proxy(server_uri)

# Call remote methods on the file server object
file_path = input("Enter the file path: ")

# Read file
content = file_server.read_file(file_path)
print("File content:")
print(content)

# Write file
content = input("Enter the content to write to the file: ")
result = file_server.write_file(file_path, content)
print(result)
