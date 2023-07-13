"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Java and Python Lab.
* Lab Experiment 6 - Implement a FTP server.
"""


from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

FTP_ADDRESS = "127.0.0.1" 
FTP_PORT = 2121
FTP_USER = "client"
FTP_PASSWORD = "password"
FTP_DIRECTORY = "./ftp_server/"

def run_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    handler.banner = "Welcome to the FTP server"

    address = (FTP_ADDRESS, FTP_PORT)
    server = servers.FTPServer(address, handler)

    server.serve_forever()

run_ftp_server()
