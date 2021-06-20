import socket
import importlib

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 65432

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
while True:
    importlib.import_module("Login")

ClientSocket.close()
