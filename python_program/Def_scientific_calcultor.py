# scientific  calcultor  using  bye def function   .....????

from math import pi, e, sin, cos, tan, log, log10, exp, sqrt

def sine():
	n = int(input("angle: "))
	a = (n * pi)/180
	return sin(a)

def cosine():
	n = int(input("angle: "))
	a = (n * pi)/180
	return cos(a)

def tangent():
	n = int(input("angle: "))
	a = (n * pi)/180
	return tan(a)

def pie():
	n = int(input("enter the no : "))
	return n * pi

def eular():
	n = int(input("enter the power find e power value : "))
	return e ** (n)

def log():
	n = int(input("enter the log base value : "))
	return log(n)

def log10():
	n = int(input("enter the log 10 base value : "))
	return 10 ** (n)
	
def exp():
	n = int(input("enter the power : "))
	m = int(input("enter the base : "))
	a = m ** (n)
	return a

def squart():
	n = int(input("enter the roots of given value : "))
	a = n ** (1/2)
	return a
	
	
print("pi, e, sin, cos, tan, log, log10, exp, sqrt")

choice = input("enter the choice of user : ")

if choice == 'pi':
	print(pie())
	
elif choice == 'e':
	print(eular())
	
elif choice == 'sin':
	print(sine())
	
elif choice == 'cos':
	print(cosine())
	
elif choice == 'tan':
	print(tangent())
	
elif choice == 'log':
	print(log())
	
elif choice == 'log10':
	print(log10())
	
elif choice == 'exp':
	print(exp())
	
elif choice == 'sqrt':
	print(squart())
	
else:
	print("user invalid key.")
	
	
	
	
'''
output ===

pi, e, sin, cos, tan, log, log10, exp, sqrt
enter the choice of user : pi
enter the no : 5
15.707963267948966


pi, e, sin, cos, tan, log, log10, exp, sqrt
enter the choice of user : sqrt
enter the roots of given value : 7896
88.85943956609225


pi, e, sin, cos, tan, log, log10, exp, sqrt
enter the choice of user : log10
enter the log 10 base value : 5
100000


pi, e, sin, cos, tan, log, log10, exp, sqrt
enter the choice of user : exp
enter the power : 1
enter the base : 9
9


pi, e, sin, cos, tan, log, log10, exp, sqrt
enter the choice of user : e
enter the power find e power value : 1
2.718281828459045


'''