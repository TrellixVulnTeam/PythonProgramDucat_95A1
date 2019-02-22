# Inherical inheritence  example in oops in class use ....??

class Bike():
	def get(self):
		self.name = input("enter the bike name : ")
		self.color = input("enter the color of bike : ")
		self.speed = int(input("enter the speed of bike : "))
		self.price = float(input("enter the price of bike : "))
		self.cc = float(input("enter the cc of bike : "))
		
	def display(self):
		print("%s\t%s\t%d\t%f\t%f"%(self.name,self.color,self.speed,round(self.price,2),round(self.cc,2)))
		# print(self.name,'\t',self.color,'\t',self.speed,'\t',self.price,'\t',self.cc)
		
class Hero(Bike):
	def __init__(self):
		print("enter the details of hero Bike : ")
		
class Honda(Bike):
	def __init__(self):
		print("enter the details of Honda Bike : ")
		
class Bajaj(Bike):
	def __init__(self):
		print("enter the details of Bajaj Bike : ")
		
class Yamaha(Bike):
	def __init__(self):
		print("enter the details of Yamaha Bike : ")
		
h1 = Hero()
h1.get()
h2 = Honda()
h2.get()
h3 = Bajaj()
h3.get()
h4 = Yamaha()
h4.get()
print("  name			color			speed			price			cc  ")
h1.display()
h2.display()
h3.display()
h4.display()




'''

output ==

enter the details of hero Bike :
enter the bike name : PASSION PRO
enter the color of bike : RED BULE
enter the speed of bike : 120
enter the price of bike : 85000
enter the cc of bike : 125.25
enter the details of Honda Bike :
enter the bike name : VIVO
enter the color of bike : BLUE
enter the speed of bike : 125
enter the price of bike : 98000
enter the cc of bike : 125.50
enter the details of Bajaj Bike :
enter the bike name : PALTINA
enter the color of bike : BLACK
enter the speed of bike : 90
enter the price of bike : 35000
enter the cc of bike : 90.5
enter the details of Yamaha Bike :
enter the bike name : YAMAHA YES
enter the color of bike : GRAY
enter the speed of bike : 180
enter the price of bike : 125000
enter the cc of bike : 220
  name   color    speed    price    cc
PASSION PRO     RED BULE        120     85000.000000    125.250000
VIVO    BLUE    125     98000.000000    125.500000
PALTINA BLACK   90      35000.000000    90.500000
YAMAHA YES      GRAY    180     125000.000000   220.000000


'''





