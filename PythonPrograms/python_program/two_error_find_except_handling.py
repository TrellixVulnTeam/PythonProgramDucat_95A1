# two error file in handle by except in handle to file error  ???

try:
	a = int(input("enter the A :"))
	b = int(input("enter the B :"))
	print(a/b)
	print("division is completed.")
except ZeroDivisionError as z:
	print(z)
except ValueError as v:
	print(v)
	
	
	
	
	
'''

output ===

enter the a :5
enter the b :0
you can not divided by zero.
enter the a :5
enter the b :0
division by zero


enter the A :5
enter the B :4
1.25
division is completed.


enter the A :5
enter the B :0
division by zero


enter the A :fdrr
invalid literal for int() with base 10: 'fdrr'

'''