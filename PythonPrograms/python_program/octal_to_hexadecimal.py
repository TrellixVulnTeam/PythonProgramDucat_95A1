# 57. Python Convert Octal to Hexadecimal  ????

octal = input("Enter any number in octal Format: ")
if octal != 'x':
    temp = int(octal, 8)
print(octal ,"in decimal =",hex(temp))



'''
output ==

Enter any number in octal Format: 065
065 in decimal = 0x35

0       3       5
     +       +                           ==    5*1 + 3 * 16 + 0 *32  ==  53    and octal value  065..     then result ouput ==  hexavalue ==  035
16**2   16**1    16**0
'''
