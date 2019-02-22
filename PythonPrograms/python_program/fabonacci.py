# Python Program to Print the Fibonacci sequence  ????

n= int(input("enter the no :")) 
a=0
b=1
print(0)
print(1)
for i in range(2,n):
	c=a+b
	a=b
	b=c
	print(c)
'''
output == 
fibonacci sequence :  === 

0 1 1 2 3 5 8 13
a=b  , b=c  , c=a+b
'''

# using recursive function the fibonacci series many terms in fast every this the fast all value in fabonacci series :  ???? 

fabonacci_value = {}

def fibonacci(n):
	# if we have cached the value , then retun it 
	if n in fibonacci_value:
		return fibonacci_value[n]

	# compute the nth term 
	if n==1:
		value=1
	elif n==2:
		value=1
	elif n>2:
		value = fibonacci(n-1) + fibonacci(n-2)

	# cache the value and return it
	fibonacci_value[n]= value
	return value

for n in range(1,1001):
	print(n,"::",fibonacci(n))