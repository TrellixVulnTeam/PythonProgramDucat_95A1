# Python Program to Convert Decimal to Binary ,octal ,hexadecimal Using Recursion   ????

def dec_bin(n):
	return bin(n)
	
def dec_oct(n):
	return oct(n)
	
def dec_hexa(n):
	return hex(n)
	
n = int(input("decimal number : "))
print("decimal to binary : ",bin(n))
print("decimal to octal : ",oct(n))
print("decimal to hexadecimal : ",hex(n))


'''

output ==

decimal number : 95
decimal to binary :  0b1011111
decimal to octal :  0o137
decimal to hexadecimal :  0x5f

'''