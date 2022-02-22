import socket
from telnetlib import SE
import tqdm
import os
import time
import argparse

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 10000 

def file_transfer(filename, host, port):

    # enter the ip address to connect to
    host = input("enter the ip of the server: ")
    # connection port
    port = 5001
    # the name of file you want to send
    file = input("enter the file you would like to tranfer (make sure you are in the same directory): ")
    # get the file size
    filesize = os.path.getsize(file)

    s = socket.socket()

    print(f"[+] connecting to {host} on {port}....")

    time.sleep(3)

    s.connect((host, port))

    print('Connected....sending file')

    s.send(f"{file}{SEPARATOR}{filesize}" .encode())

    #send the file
    progress = tqdm.tqdm(range(filesize), f"Sending {file}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(file, "rb") as f:
        while True:
            #how big is the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # done transmitting
                break
            
            s.sendall(bytes_read)
            # progress bar
            progress.update(len(bytes_read))

    s.close()

    print('file sent succesfully!')

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple File Sender")
    parser.add_argument("file", help="File to send")
    parser.add_argument("host", help="The ip of the receiver")
    parser.add_argument("-p", "--port", help="default port is 5001", default=5001)
    args = parser.parse_args()
    filename = args.file
    host = args.host
    port = args.port
    file_transfer(filename, host, port)




