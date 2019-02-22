import socket
hostname = socket.gethostname()
IP_add = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IP_add)