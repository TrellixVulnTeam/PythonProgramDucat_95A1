# 54. Python Binary to Hexadecimal  ????

binary = input("Enter any number in Binary Format: ");
if binary != 'x':
    temp = int(binary, 2)
print(binary,"in hexadecimal =",hex(temp))


'''
output ==

Enter any number in Binary Format: 101011010
101011010 in hexadecimal  = 0x15a

'''