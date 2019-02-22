# Python Program to Find LCM (Largest numbers.. )  ????


n= int(input("enter the number: "))   
m= int(input("enter the number: ")) 
a=n
b=m  
if m > n :
	while m > n:  
		m = m - n
		hcf = m
	print("hcf of two numbers : ",hcf)
	lcm = (a*b)// hcf
	print("lcm of two number : ",lcm)
else:	
	while n > m:
		n = n - m
		hcf = n
	print("hcf of two numbers : ",hcf)
	lcm = (a*b)// hcf
	print("lcm of two number : ",lcm)

	
	
'''
enter the number: 105
enter the number: 45
hcf of two numbers :  15
lcm of two number :  315
'''