from ftplib import FTP

FTP_ADDRESS = "127.0.0.1"
FTP_PORT = 2121
FTP_USER = "client"
FTP_PASSWORD = "password"

def ftp_client():
    ftp = FTP()
    ftp.connect(FTP_ADDRESS, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASSWORD)

    print("Current directory:", ftp.pwd())
    print("Files:")
    ftp.retrlines('LIST')

    directory = "./text_files/"
    ftp.cwd(directory)
    print("Changed directory:", ftp.pwd())

    local_file = "./client.txt"
    remote_file = "./server.txt"
    with open(local_file, "rb") as file:
        ftp.storbinary(f"STOR {remote_file}", file)
    print("File uploaded successfully.")

    local_file = "./download.txt"
    remote_file = "./server.txt"
    with open(local_file, "wb") as file:
        ftp.retrbinary(f"RETR {remote_file}", file.write)
    print("File downloaded successfully.")

    ftp.quit()

ftp_client()
