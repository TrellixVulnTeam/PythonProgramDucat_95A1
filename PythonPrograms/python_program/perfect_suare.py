from math import sqrt
num=int(input("Enter the Number :  "))
x=int(sqrt(num))
if(x*x==num):
	print("Perfect Square Number")
else:
	print("Not Perfect Square Number")
