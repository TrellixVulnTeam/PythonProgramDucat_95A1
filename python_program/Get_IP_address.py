# Python Program - Get IP Address

import socket
print("Want to get IP Address ? (y/n): ");
check = input();
if check == 'n':
    exit();
else:
    print("\nYour IP Address is: ",end="")
    print(socket.gethostbyname(socket.gethostname()))
	
'''
output ===
Want to get IP Address ? (y/n):
y

Your IP Address is: 192.168.0.102

'''