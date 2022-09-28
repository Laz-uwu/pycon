import socket
from psd_tools import  PSDImage

def reciever():
    print("[STARTING] Server is starting.")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(ADDR)

    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT))

        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))

        file.close()

        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

def sender_all():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(ADDR)

    file = open("data/yt.txt", "r")
    data = file.read()

    client.send("yt.txt".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    file.close()

    client.close()

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def psd_thumbnail():
    #PSDImage.open(psdfile).thumbnail().save(new_file_name)
    print("")

def tiff_thumbnail():
    print("")

def file_transfer(psdfile):
    print("FILE TRANSFER ",psdfile)
    print("")
