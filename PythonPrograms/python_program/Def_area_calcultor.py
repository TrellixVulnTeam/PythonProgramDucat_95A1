# area calcultor use by def function ...????

def rectangle():
	n = float(input("enter the length cm :: "))
	l = float(input("enter the breadth cm :: "))
	a = n * l
	b = a / 10**4
	c = a * 100
	d = a / 10**8
	e = a / 10**14
	f = a * (0.011) * (0.011)
	g = a * (0.032) * (0.032)
	print("area of rectangle in cm**2 : ",a," cm**2")
	print("area of rectangle in meter**2 : ",b," meter**2")
	print("area of rectangle in mm**2 : ",c," mm**2")
	print("area of rectangle in km**2 : ",d," km**2")
	print("area of rectangle in ton**2 : ",e," ton**2")
	print("area of rectangle in yard**2 : ",f," yard**2")
	print("area of rectangle in feet**2 : ",g," feet**2")
	
def square():
	n = float(input("enter the side cm :: "))
	a = n * n
	b = a / 10**4
	c = a * 100
	d = a / 10**8
	e = a / 10**14
	f = a * (0.011) * (0.011)
	g = a * (0.032) * (0.032)
	print("area of square in cm**2 : ",a," cm**2")
	print("area of square in meter**2 : ",b," meter**2")
	print("area of square in mm**2 : ",c," mm**2")
	print("area of square in km**2 : ",d," km**2")
	print("area of square in ton**2 : ",e," ton**2")
	print("area of square in yard**2 : ",f," yard**2")
	print("area of square in feet**2 : ",g," feet**2")
	
def triangle():
	side1 = float("enter the side in cm : ")
	side2 = float("enter the side in cm : ")
	side3 = float("enter the side in cm : ")
	per = ( side1 + side2 + side3 )/ 2
	area_triangle = (per * (per - side1) * (per - side2) * (per - side3)) ** (1/2)
	b = area_triangle / 10**4
	c = area_triangle * 100
	d = area_triangle / 10**8
	e = area_triangle / 10**14
	f = area_triangle * (0.011) * (0.011)
	g = area_triangle * (0.032) * (0.032)
	print("area of traingle is cm **2 : ",area_triangle,"cm**2")
	print("area of traingle in meter**2 : ",b," meter**2")
	print("area of traingle in mm**2 : ",c," mm**2")
	print("area of traingle in km**2 : ",d," km**2")
	print("area of traingle in ton**2 : ",e," ton**2")
	print("area of triangle in yard**2 : ",f," yard**2")
	print("area of triangle in feet**2 : ",g," feet**2")
	
def remobus():
	base = float(input("enter the base value : "))
	height = float(input("enter the height value : "))
	area_remobus = base * height
	b = area_remobus / 10**4
	c = area_remobus * 100
	d = area_remobus / 10**8
	e = area_remobus / 10**14
	f = area_remobus * (0.011) * (0.011)
	g = area_remobus * (0.032) * (0.032)
	print("area of remobus in cm : ",area_remobus," cm**2")
	print("area of remobus in meter**2 : ",b," meter**2")
	print("area of remobus in mm**2 : ",c," mm**2")
	print("area of remobus in km**2 : ",d," km**2")
	print("area of remobus in ton**2 : ",e," ton**2")
	print("area of remobus in yard**2 : ",f," yard**2")
	print("area of remobus in feet**2 : ",g," feet**2")
	
	
print("rectangle , square , triangle , remobus .")

choice = input("enter the user choice : ")

if choice == 'rectangle':
	rectangle()
	
elif choice == 'square':
	square()
	
elif choice == 'triangle':
	triangle()
	
elif choice == 'remobus':
	remobus()
	
else:
	print("invalid key.")
	
	
	
'''
output ===

rectangle , square , triangle , remobus .
enter the user choice : rectangle
enter the length cm :: 12
enter the breadth cm :: 15
area of rectangle in cm**2 :  180.0  cm**2
area of rectangle in meter**2 :  0.018  meter**2
area of rectangle in mm**2 :  18000.0  mm**2
area of rectangle in km**2 :  1.8e-06  km**2
area of rectangle in ton**2 :  1.8e-12  ton**2
area of rectangle in yard**2 :  0.021779999999999997  yard**2
area of rectangle in feet**2 :  0.18431999999999998  feet**2


rectangle , square , triangle , remobus .
enter the user choice : remobus
enter the base value : 45
enter the height value : 48
area of remobus in cm :  2160.0  cm**2
area of remobus in meter**2 :  0.216  meter**2
area of remobus in mm**2 :  216000.0  mm**2
area of remobus in km**2 :  2.16e-05  km**2
area of remobus in ton**2 :  2.16e-11  ton**2
area of remobus in yard**2 :  0.26136  yard**2
area of remobus in feet**2 :  2.21184  feet**2


rectangle , square , triangle , remobus .
enter the user choice : square
enter the side cm :: 80
area of square in cm**2 :  6400.0  cm**2
area of square in meter**2 :  0.64  meter**2
area of square in mm**2 :  640000.0  mm**2
area of square in km**2 :  6.4e-05  km**2
area of square in ton**2 :  6.4e-11  ton**2
area of square in yard**2 :  0.7743999999999999  yard**2
area of square in feet**2 :  6.5536  feet**2


'''