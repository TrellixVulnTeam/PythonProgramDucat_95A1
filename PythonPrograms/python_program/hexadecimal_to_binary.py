# 59. Python Hexadecimal to Binary   ???

hexadecimal = input("Enter number in hexadecimal Format: ")
if hexadecimal != 'x':
    decimal = int(hexadecimal, 16)
print(hexadecimal,"in Decimal =",bin(decimal))


'''
output ==

Enter number in hexadecimal Format: 035
035 in Decimal = 0b110101

'''
