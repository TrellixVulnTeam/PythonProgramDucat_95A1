# Python Program To Display Powers of 2 and (1/2 (square roots)) Using Anonymous Function  ???

n=int(input("enter the number of range : "))
for i in range(1,n+1):
	a = i ** 2
	b = i ** (1/2)
	print(i," power (2) == ",a)
	print(b," square root == ",round(b,3))
'''
output === 
enter the number of range : 5
1  power (2) ==  1
1.0  square root ==  1.0
2  power (2) ==  4
1.4142135623730951  square root ==  1.4142135623730951
3  power (2) ==  9
1.7320508075688772  square root ==  1.7320508075688772
4  power (2) ==  16
2.0  square root ==  2.0
5  power (2) ==  25
2.23606797749979  square root ==  2.23606797749979

'''


# another mathod using by the only one no not in range :  ???

p= int(input("enter the number : "))
a = p ** 2
b = p ** (1/2)
print(p,"** (2) == ",a)
print(p,"square root of == ",round(b,3))

'''
output === 
enter the number : 941
941 ** (2) ==  885481
941 square root of ==  30.675723300355934
'''