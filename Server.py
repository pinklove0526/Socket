import socket
import tkinter

HOST = "127.0.0.1"
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("Waiting for client")
conn, addr = accept()
try:
    print("Connected by: ", addr)
    while True:
        data = conn.recv(1024)
        if len(data) > 0:
            print("Server receive: " + data.decode("utf8"))
    except KeyboardInterrupt:
        conn.close()
    finally:
        conn.close()