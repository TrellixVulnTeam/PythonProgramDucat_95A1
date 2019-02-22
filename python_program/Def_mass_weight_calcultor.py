# weigth and mass calcultor used by def function ...???

# kilogram = pound , carats = pound , miligram , centigram ,decigram , gram ,decagram , hectogram , kilogram , ton , ounces.

def pound():
	n = float(input("enter the pound : "))
	m = float(input("enter the kg : "))
	a = n * (0.45)
	b = m / (0.45)
	print("convert the pound to kilogram : ",a,"kg")
	print("convert the kilogram to pound : ",b,"pound")
	
def carat():
	n = float(input("enter the carat : "))
	m = float(input("enter the pound : "))
	a = n * (0.00044)
	b = m / (0.00044)
	print("convert the carat to pound : ",a,"pound")
	print("convert the pound to carat : ",b,"carat")
	
def ounces():
	n = float(input("enter the ounces : "))
	m = float(input("enter the grams : "))
	a =  n * (28.35)
	b = m / (28.35)
	print("convert the ounces to gram : ",a,"gram")
	print("convert the gram to ounces : ",b,"ounces")
	
def gram():
	n = float(input("enter the gram : "))
	mg = n *(1000)
	cg = n * (100)
	dg = n * (10)
	dg = n / 10
	hg = n / (100)
	kg = n / (1000)
	ton = n / (10 ** 6)
	
	print("convert gram to miligram : ",mg,"mg")
	print("convert gram to centigram : ",cg,"cg")
	print("convert gram to decigram : ",dg,"dg")
	print("convert gram to decagram : ",dg,"dg")
	print("convert gram to hectogram : ",hg,"hg")
	print("convert gram to kilogram : ",kg,"kg")
	print("convert gram to ton: ",ton,"ton")
	
	
def ton():
	n = float(input("enter the ton : "))
	gram = n / (10 ** 6)
	mg = n / (10 ** 9)
	cg = n / (10 ** 8)
	dg = n / (10 ** 7)
	dg = n / (10 ** 5)
	hg = n / (10 ** 4)
	kg = n / (1000)
	ton = n * 1
	
	print("convert ton to gram : ",gram,"gram")
	print("convert ton to miligram : ",mg,"mg")
	print("convert ton to centigram : ",cg,"cg")
	print("convert ton to decigram : ",dg,"dg")
	print("convert ton to decagram : ",dg,"dg")
	print("convert ton to hectogram : ",hg,"hg")
	print("convert ton to kilogram : ",kg,"kg")
	print("convert ton to ton : ",ton,"ton")
	
	
	
print("pound , carat ,ounces , gram , ton .")

choice = input("enter the choice of user : ")

if choice == 'pound':
	pound()
	
elif choice == 'carat':
	carat()
	
elif choice == 'ounces':
	ounces()
	
elif choice == 'gram':
	gram()
	
elif choice == 'ton':
	ton()
	
else:
	print("invalid key.")

	
	
'''
output ===


pound , carat ,ounces , gram , ton .
enter the choice of user : ton
enter the ton : 4502136
convert ton to gram :  4.502136 gram
convert ton to miligram :  0.004502136 mg
convert ton to centigram :  0.04502136 cg
convert ton to decigram :  45.02136 dg
convert ton to decagram :  45.02136 dg
convert ton to hectogram :  450.2136 hg
convert ton to kilogram :  4502.136 kg
convert ton to ton :  4502136.0 ton


pound , carat ,ounces , gram , ton .
enter the choice of user : gram
enter the gram : 456
convert gram to miligram :  456000.0 mg
convert gram to centigram :  45600.0 cg
convert gram to decigram :  45.6 dg
convert gram to decagram :  45.6 dg
convert gram to hectogram :  4.56 hg
convert gram to kilogram :  0.456 kg
convert gram to ton:  0.000456 ton


pound , carat ,ounces , gram , ton .
enter the choice of user : carat
enter the carat : 456
enter the pound : 456
convert the carat to pound :  0.20064 pound
convert the pound to carat :  1036363.6363636364 carat


pound , carat ,ounces , gram , ton .
enter the choice of user : ounces
enter the ounces : 45
enter the grams : 45
convert the ounces to gram :  1275.75 gram
convert the gram to ounces :  1.5873015873015872 ounces


'''