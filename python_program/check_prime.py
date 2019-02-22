#  Python Check Prime or Not  ????

while True:
	print("enter 'x' for exit.")
	n = int(input("enter the number : "))
	if n == 'x':
		break
	else:
		for i in range(2,n):
			if n%i == 0:
				print(n,"number is not prime.\n")    # \n is enter the new line in program.
				break
		else:
			print(n,"number is prime.\n")

			
'''
output ==
Python Check Prime or Not ===
enter 'x' for exit.
enter the number : 45
45 number is not prime.

enter 'x' for exit.
enter the number : 89
89 number is prime.
 
'''

#   another simple mathod of prime number check ....???

m = int(input("enter the number: "))
for i in range(2,m):
	if m % i == 0:
		print(m,"is not prime.")
		break
else:
	print(m,"is prime.")
	
	
'''
output ==
enter the number : 89
89 number is prime.
'''