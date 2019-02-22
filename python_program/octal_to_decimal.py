# 55. Python Convert Octal to Decimal  ????

octal = input("Enter any number in Binary Format: ")
if octal != 'x':
    temp = int(octal, 8)
print(octal ,"in decimal =",(temp))


'''
output ===

Enter any number in Binary Format: 065
065 in decimal = 53

#  0    6    5 
      +     +        ==  5*(8**0)  +  6 * (8**1)  + 0 * (8**2 ) ==  53
  8*2  8**1  8**0

#  hexadecimal in multiple backside 16 ** power 2  + last digit  =====   to first digit and after add but back right to left value power increased 0,1,2,3,4...???  
  
'''