#  Python Find Factorial of a Number  ???

n = int(input("enter the number : "))

fact=1
while n > 0:
	fact = fact * (n)
	n = n-1
print("total fact number value :",fact)

'''
output ==
enter the number : 5
total fact number value : 120

'''