import socket
s=socket.socket()
host='localhost'
print(host)
port=12348
s.connect((host,port))
s.listen(12348)
print(s.recv(1024))
s.close()