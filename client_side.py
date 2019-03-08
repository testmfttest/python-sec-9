import socket
socket = socket.socket()
socket.connect(("127.0.0.1",12345))
data = socket.recv(8192)
menu = data.decode()
print(menu)
choice = input("choice a menu item")
socket.send(choice.encode())
filename = menu.split("\n")[int(choice)-1]
filename = filename.lstrip("0123456789-")
file = open(filename , "wb")
file.write(socket.recv(1000000))
file.close()
