'''
except error handling use only four conditios ..??

1. try :
2. except :  ==>>  try only use condtion all solution of program and except to all error in handling to all values..??
3. finally :
4. raise :

'''

# file handling to zero handling errors ...??

a = int(input("enter the a :"))
b = int(input("enter the b :"))
try:
	print(a/b)
	print("division is completed.")
except:
	print("you can not divided by zero.")
	
	
	
	
# file handling to zero handling errors ...??

a = int(input("enter the a :"))
b = int(input("enter the b :"))
try:
	print(a/b)
	print("division is completed.")
except ZeroDivisionError as z:                        # z like as the zeroerror type .
	print(z)
	
	
	
	
'''

output ===

enter the a :5
enter the b :0
you can not divided by zero.

enter the a :5
enter the b :2
2.5
division is completed.
you can not divided by zero.

enter the a :5
enter the b :0
division by zero

'''