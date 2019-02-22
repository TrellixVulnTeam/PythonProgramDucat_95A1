# 56. Python Convert Octal to Binary   ???

octal = input("Enter any number in octal Format: ")
if octal != 'x':
    temp = int(octal, 8)
print(octal ,"in decimal =",bin(temp))


'''
output ===

Enter any number in octal Format: 065
065 in decimal = 0b110101

'''