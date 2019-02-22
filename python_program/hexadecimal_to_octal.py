# 60. Python Convert Hexadecimal to Octal  ????

hexadecimal = input("Enter number in hexadecimal Format: ")
if hexadecimal != 'x':
    decimal = int(hexadecimal, 16)
print(hexadecimal,"in Decimal =",oct(decimal))


'''
output ===

Enter number in hexadecimal Format: 035
035 in Decimal = 0o65

'''