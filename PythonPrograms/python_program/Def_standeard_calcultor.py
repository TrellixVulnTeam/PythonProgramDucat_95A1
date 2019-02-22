# standeard  calcultor  using by def ...???

def add():
	a = int(input("A : "))
	b = int(input("B : "))
	c = a + b
	return c
	
def sub():
	a = int(input("A : "))
	b = int(input("B : "))
	c = a - b
	return c

def mul():
	a = int(input("A : "))
	b = int(input("B : "))
	c = a * b
	return c

def div():
	a = int(input("A : "))
	b = int(input("B : "))
	c = a / b
	return c
	
def root():
	a = int(input("A : "))
	c = a ** (1/2)
	return round(c,4)
	
def square():
	a = int(input("A : "))
	c = a ** (2)
	return c
	
def inverse():
	a = int(input("A : "))
	c = 1 / a
	return round(c,4)                        


print("+,-,*,/,root,square,inverse.")

choice = input("enter the choice of user : ")

if choice == '+':
	print(add())
	
elif choice == '-':
	print(sub())
	
elif choice == '*':
	print(mul())
	
elif choice == '/':
	print(div())
	
elif choice == 'root':
	print(root())
	
elif choice == 'square':
	print(square())
	
elif choice == 'inverse':
	print(inverse())
	
else:
	print("user invalid key.")
	
	
'''
output ===

+,-,*,/,root,square,inverse.
enter the choice of user : *
A : 5
B : 6
30

+,-,*,/,root,square,inverse.
enter the choice of user : root
A : 96
9.798

+,-,*,/,root,square,inverse.
enter the choice of user : inverse
A : 5
0.2

'''