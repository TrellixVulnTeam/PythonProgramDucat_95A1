# angle calcultor used by def function ....????

# degree , gradians  , radians  *****



def degree():
	n = float(input("enter the radians : "))
	m = float(input("enter the gradians : "))
	d = n * (57.30)
	e = m * (0.9)
	print("convert the radians to degree : ",d," *d")
	print("convert the gradians to degree : ",e," *d")
	
def radian():
	n = float(input("enter the degree : "))
	m = float(input("enter the gradians : "))
	d = n * (0.017) 
	e = m * (0.015)
	print("convert the degree to radians : ",d," *r")
	print("convert the gradians to radians : ",e," *r")
	
def gradian():
	n = float(input("enter the degree : "))
	m = float(input("enter the radians : "))
	d = n * (1.11)
	e = m * (63.66)
	print("convert the degree to gradians: ",d," *g")
	print("convert the radians to gradians : ",e," *g")
	
	
print("degree , radian , gradian. ")

choice = input("enter the user choice : ")

if choice == 'degree':
	degree()
	
elif choice == 'radian':
	radian()
	
elif choice == 'gradian':
	gradian()
	
else:
	print("invalid key.")
	
	
	
'''
output ===

degree , radian , gradian.
enter the user choice : radian
enter the degree : 45
enter the gradians : 78
convert the degree to radians :  0.765  *r
convert the gradians to radians :  1.17  *r


degree , radian , gradian.
enter the user choice : degree
enter the radians : 108
enter the gradians : 180
convert the radians to degree :  6188.4  *d
convert the gradians to degree :  162.0  *d


degree , radian , gradian.
enter the user choice : gradian
enter the degree : 100
enter the radians : 100
convert the degree to gradians:  111.00000000000001  *g
convert the radians to gradians :  6366.0  *g


'''