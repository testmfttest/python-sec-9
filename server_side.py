import socket
import time
socket = socket.socket()
socket.bind(("127.0.0.1" , 12345))
socket.listen(5)
while True:
    conn, address = socket.accept()
    html= """
    <head>
  <meta http-equiv="refresh" content="1">
</head>
    """
    date = "<h1>"+str(time.ctime())+"</h1>"
    date = html+date
    header = "HTTP/1.1 200 OK\n"
    header+= "Content-Type: text/html\n"
    header+= "Content-Length: "+str(len(date))+"\n\n"
    conn.send((header+date).encode())