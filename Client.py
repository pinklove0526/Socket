import socket
import importlib

ClientSocket = socket.socket()
HOST = '127.0.0.1'
PORT = input('Nhap port cua server: ')

print('Dang cho ket noi')
try:
    ClientSocket.connect((HOST, PORT))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
while True:
    importlib.import_module("Login")

ClientSocket.close()
