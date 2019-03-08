import socket
import time
import os
files = None
def find_files():
    global files
    files = os.listdir(r"C:\Users\Net\Desktop\data")
    print(files)
    menu = ""
    for index , file in enumerate(files):
        menu += f"{index+1}-{file}\n"
    return menu
socket = socket.socket()
socket.bind(("127.0.0.1" , 12345))
socket.listen(5)
while True:
    conn, address = socket.accept()
    conn.send(find_files().encode())
    choice = conn.recv(1024).decode().strip()
    file= files[int(choice)-1]
    data = open(r"C:\Users\Net\Desktop\data\\"+file , "rb")
    data = data.read()
    conn.send(data)


