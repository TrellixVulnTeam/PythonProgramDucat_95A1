#  programmer  calcultor  used by def mathod ...????


def decimal():
	decimal = input("Enter number in decimal Format: ")
	if decimal != 'x':
		decimal = int(decimal)
		a = (bin(decimal),oct(decimal),hex(decimal))
		for x in a:
			print(x)
		else:
			exit()
			
	
def binary():
	binary = input("Enter number in binary Format: ")
	if binary != 'x':                                            # used condition this is the binary value base on 2 another value print so break no print value excepted ...???
		decimal = int(binary, 2)
		a = ((decimal),oct(decimal),hex(decimal))
		for x in a:
			print(x)
		else:
			exit()
			
			
def octal():
	octal = input("Enter number in octal Format: ")
	if octal != 'x':
		decimal = int(octal, 8)
		a = ((decimal),bin(decimal),hex(decimal))
		for x in a:
			print(x)
		else:
			exit()
			
			
def hexadecimal():
	hexadecimal = input("Enter number in hexadecimal Format: ")
	if hexadecimal != 'x':
		decimal = int(hexadecimal, 16)
		a = ((decimal),bin(decimal),oct(decimal))
		for x in a:
			print(x)
		else:
			exit()
			
			
print("decimal , binary , octal , hexadecimal")

choice = input("user choice value : ")

if choice == 'decimal':
	decimal()
	
elif choice == 'binary':
	binary()
	
elif choice == 'octal':
	octal()
	
elif choice == 'hexadecimal':
	hexadecimal()
	
else:
	print("invalid key.")
	
	
	
'''

output ===


decimal , binary , octal , hexadecimal
user choice value : hexadecimal
Enter number in hexadecimal Format: 56
86
0b1010110
0o126


decimal , binary , octal , hexadecimal
user choice value : octal
Enter number in octal Format: 56
46
0b101110
0x2e


'''