# Python Program to Display Fibonacci Sequence Using Recursion  ????

def fibo(n):
	if n == 1:
		return 0

	elif n == 2:
		return 1
		
	elif n > 2:
		return (fibo(n-1) + fibo(n-2))
		
m= int(input("enter the range : "))
for n in range(1,m+1):
	print(n ,'term of fibonacci series : ',fibo(n))


'''
output == 
1 term of fibonacci series :  0
2 term of fibonacci series :  1
3 term of fibonacci series :  1
4 term of fibonacci series :  2
5 term of fibonacci series :  3
6 term of fibonacci series :  5
7 term of fibonacci series :  8
8 term of fibonacci series :  13
9 term of fibonacci series :  21
10 term of fibonacci series :  34
11 term of fibonacci series :  55
12 term of fibonacci series :  89
13 term of fibonacci series :  144
14 term of fibonacci series :  233
15 term of fibonacci series :  377
'''
		
		
		
# Python program to display the Fibonacci sequence up to n-th term using recursive functions

"""Recursive function to
   print Fibonacci sequence"""
   
def re_fibo(n):     
   
   if n <= 1:          
       return n
   else:
       return(re_fibo(n-1) + re_fibo(n-2))     

# Change this value for a different result
# nterms = 10

# uncomment to take input from the user
terms = int(input("How many terms? "))

# check if the number of terms is valid
if terms <= 0:         
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(terms):
       print(re_fibo(i))
	   
	   
'''
output == 
How many terms? 12
Fibonacci sequence:
0
1
1
2
3
5
8
13
21
34
55
89

'''

