# Python Solve Quadratic Equation   ???

print("a x** (2) + b x + c = 0 :  ")
a = int(input("enter the number : "))
b = int(input("enter the number : "))
c = int(input("enter the number : "))

D = b ** (2) - 4 * a * c
if D > 0:
	("two_roots...")
	root1 = (-b + D )/ (2 * a)
	root2 = (-b - D )/ (2 * a)
	print("Quadratic roots : ",root1,"&",root2)
elif D == 0:
	("one_root...")
	root1 = -b / (2 * a)
	print("Quadratic roots : ",root1)
else:
	print("Quadratic is complex : ",D)
	print("Quadratic equation has no_roots .")
	
'''
output ==

1************************
a x** (2) + b x + c = 0 :
enter the number : 1
enter the number : 2
enter the number : 1
Quadratic roots :  -1.0

2************************
a x** (2) + b x + c = 0 :
enter the number : 4
enter the number : 9
enter the number : 17
Quadratic equation has no_roots .

3************************
a x** (2) + b x + c = 0 :
enter the number : 5
enter the number : 9
enter the number : 7
-59 D is complex so
Quadratic equation has no_roots .

4************************
a x** (2) + b x + c = 0 :
enter the number : 2
enter the number : -4
enter the number : -4
Quadratic roots :  13.0 & -11.0

'''