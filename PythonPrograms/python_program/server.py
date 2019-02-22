import socket as f
s=f.socket()
print(s)
host='localhost'
port=12348
s.bind((host,port))
s.listen(1)
while True:
	c,addr=s.accept()
	print("Get Connection from",addr)
	print("Get Connection from",c)
	c.send(b"Thank")
c.close()