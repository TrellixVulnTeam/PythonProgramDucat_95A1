# Python Program to Find Factorial of Number Using Recursion  ????    (while loop used in def function .)

def fact(n):
	i=1
	fact=1
	while n > i:
		fact = fact * n
		n = n-1
	return (fact)

n= int(input("enter the number output in factorial : "))
print("factorial of given number : ",fact(n))

'''

output == 
enter the number output in factorial : 10
factorial of given number :  3628800 

'''


# using def find the factorial of the given number (use the for loop . ) ????

def fact(n):
	fact=1
	for i in range(n,0,-1):
		fact = fact * i	
	return fact

n = int(input("range : "))
print("factorial of the number : ",fact(n))

'''

output == 
range : 10
factorial of the number :  3628800

'''