import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 65432
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Dang cho ket noi...')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Chao mung den voi server!'))
    while True:
        data = connection.recv(1024)
        reply = 'Server tra loi: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Da ket noi den: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('So ket noi: ' + str(ThreadCount))
ServerSocket.close()
