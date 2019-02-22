# Python Program - Convert Binary to Octal

binary = input("Enter any number in Binary Format: ");
if binary != 'x':
    temp = int(binary, 2)
print(binary,"in Octal =",oct(temp))


'''
output ===

Enter any number in Binary Format: 10101011
10101011 in Octal = 0o253


'''