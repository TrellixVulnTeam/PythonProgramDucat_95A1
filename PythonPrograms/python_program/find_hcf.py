# Python Program to Find HCF or GCD  ????


n= int(input("enter the number: "))   
m= int(input("enter the number: "))   
if m > n :
	while m > n:  
		m = m - n    
	print("hcf of two numbers : ",m)
else:	
	while n > m:
		n = n - m
	print("hcf of two numbers : ",n)

	

	
'''
15
35
output ==
hcf == 5
'''


