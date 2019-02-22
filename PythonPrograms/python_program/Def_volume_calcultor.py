# volume calcultor used by def function ....????

def meter():
	n = float(input("enter the meter : "))
	mm = n * 1000
	cm = n / 100
	km = n / 1000
	print("meter to mm : ",mm,"milimeter")
	print("meter to cm : ",cm,"centimeter")
	print("meter to km : ",km,"kilometer")
	
def litre():
	n = float(input("enter the litre :"))
	ml = n * 1000
	cl = n / 100
	kl = n / 1000
	print("liter to ml : ",ml,"mililitre")
	print("liter to cl : ",cl,"centilitre")
	print("liter to kl : ",kl,"kilolitre")
	
def cubiclitre():
	n = float(input("enter the litre : "))
	c = n ** (3)
	print(c,"cube.Litre")
	
def cubicmeter():
	n = float(input("enter the meter : "))
	c = n ** (3)
	print(c,"cubeCm.")

def inch():
	n = float(input("enter the inch : "))
	m = float(input("enter the cm : "))
	c = n  * (2.54)
	d = m  / (2.54)
	print("convert the inch to cm : ",c,"cm.")
	print("convert the cm to inch : ",d,"inch.")

def feet():
	n = float(input("enter the feet : "))
	m = float(input("enter the cm : "))
	o = float(input("enter the inch : "))
	a = n * (31.5)
	b = m / (31.5)
	c = o * (2.54)
	d = m / (2.54)
	e = n * 12
	f = o / 12
	print("convert the feet to cm : ",a,"cm.")
	print("convert the cm to feet : ",b,"feet")
	print("convert the inch to cm : ",c,"cm.")
	print("convert the cm to inch : ",d,"inch.")
	print("convert the feet to inch : ",e,"inch.")
	print("convert the inch to feet : ",f,"feet.")
	
def yard():
	n = float(input("enter the meter : "))
	m = float(input("enter the yard : "))
	c = m / (0.91)
	d = m * (0.91) 
	print("convert meter to yard : ",c,"yard")
	print("convert yard to meter : ",d,"meter")

def gallon():
	n = float(input("enter the gallon : "))
	m = float(input("enter the litre: "))
	c = n * (3.8)
	d = m / (3.8)
	print("convert the gallon to litre : ",c,"litre")
	print("convert the litre to gallon : ",d,"gallon")

def quart():
	n = float(input("enter the quart : "))
	m = float(input("enter the litre : "))
	c = n * (1.1)
	d = n / (1.1)
	print("convert quart to liter : ",c,"litre")
	print("convert litre to quart ",d,"quart")

	
print("meter , litre , cubiclitre , cubicmeter , inch , feet , yard ,gallon , quart .")
		
choice = input("enter the user choice : ")

if choice == 'meter':
	meter()
	
elif choice == 'litre':
	litre()
	
elif choice == 'cubiclitre':
	cubiclitre()
	
elif choice == 'cubicmeter':
	cubicmeter()
	
elif choice == 'inch':
	inch()
	
elif choice == 'feet':
	feet()
	
elif choice == 'yard':
	yard()
	
elif choice == 'gallon':
	gallon()
	
elif choice == 'quart':
	quart()
	
	
	
'''
output ===

meter , litre , cubiclitre , cubicmeter , inch , feet , yard ,gallon , quart .
enter the user choice : meter
enter the meter : 100
meter to mm :  100000.0 milimeter
meter to cm :  1.0 centimeter
meter to km :  0.1 kilometer


meter , litre , cubiclitre , cubicmeter , inch , feet , yard ,gallon , quart .
enter the user choice : yard
enter the meter : 1.25
enter the yard : 2.25
convert meter to yard :  2.4725274725274726 yard
convert yard to meter :  2.0475 meter


meter , litre , cubiclitre , cubicmeter , inch , feet , yard ,gallon , quart .
enter the user choice : gallon
enter the gallon : 3.78
enter the litre: 3.78
convert the gallon to litre :  14.363999999999999 litre
convert the litre to gallon :  0.9947368421052631 gallon


meter , litre , cubiclitre , cubicmeter , inch , feet , yard ,gallon , quart .
enter the user choice : cubicmeter
enter the meter : 1230
1860867000.0 cubeCm.

'''