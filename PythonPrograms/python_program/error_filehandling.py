a = int(input("a:"))
b = int(input("b:"))
try:
	print(a/b)
	print("division is complete.")
except ZeroDivisionError as z:
	print(z)