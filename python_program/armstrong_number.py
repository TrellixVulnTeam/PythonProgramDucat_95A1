# Python Program to Check Armstrong Number  ????

n= int(input("enter the number : "))
temp=n
sum=0
while n > 0:
	digit= n%10
	sum = sum + digit**3
	n=n//10
print(sum)
if temp == sum:
	print("this is armstrong number.")
else:
	print("this is not armstrong number.")
	
	
'''
output === 
n=371
this is armstrong number.
'''