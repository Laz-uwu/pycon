import socket
import sys

host=socket.gethostbyname(socket.gethostname())
port = 4455
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

msg = s.recv(1024)
print(msg.decode("utf-8"))
s.send(bytes("RECIEVED","utf-8"))