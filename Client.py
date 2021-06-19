import socket
import tkinter

HOST = "127.0.0.1"
PORT = 65432

client = socket.socket(soket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print("Client connecting to server with port: " + str(PORT))
client.connect(server_address)

try:
    while True:
        msg = input('Client: ')
        client.sendall(bytes(msg, "utf8"))
    except KeyboardInterrupt:
        client.close()
    finally:
        client.close()