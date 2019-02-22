a=int(input("Enter the First Number : "))#5
b=int(input("Enter the Second Number : "))#0
try:
	print(a/b)
	print("Division is Complete")
except ZeroDivisionError as ab:
	print(ab)
	
	
