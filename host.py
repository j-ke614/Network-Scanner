from http import client
import socket
from cv2 import add
import tqdm
import os


# device's IP address
SERVER_HOST = "192.168.3.10"
SERVER_PORT = 5001

BUFFER_SIZE = 10000
SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

#server listens for connections

s.listen(10)

print(f'[*] Listening as {SERVER_HOST} on {SERVER_PORT}')

#server accepts the connection

client_socket, address = s.accept()

#notify user of connection

print(f'[+] {address} is connected')

received = client_socket.recv(BUFFER_SIZE).decode()

filename, filesize = received.split(SEPARATOR)

#remove path if present

file = os.path.basename(filename)

filesize = int(filesize)

# start receiving the file 
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    while True:
        
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:    
            # nothing is received

            break
        
        f.write(bytes_read)
        #progress bar
        progress.update(len(bytes_read))

# close client connection
client_socket.close()
# close  server connection
s.close()




