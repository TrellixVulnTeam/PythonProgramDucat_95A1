# power , data , pressure .....

# power calcultor used by def function ...???

def watt():
	w = float(input("enter the watt :"))
	a = w / 220
	hp = w / 746
	kw = w / 1000
	print("convert watt to amp : ",a," amp")
	print("convert watt to horsepower : ",a," hp")
	print("convert watt to kilowalt : ",a," kw")
	
def kilowatt():
	kw = float(input("enter the kilowalt :"))
	w = kw / 1000
	a = w / 220
	hp = w / 746
	print("convert kilowatt to walt : ",w," kw")
	print("convert kilowatt to amp : ",a," amp")
	print("convert kilowatt to horsepower : ",hp," hp")
	
def amp():
	a = float(input("enter the amp :"))
	w = a * 220
	kw = w * 1000
	hp = w / 746
	print("convert amp to walt : ",w," w")
	print("convert amp to kilowatt : ",kw," amp")
	print("convert amp to horsepower : ",hp," hp")
	
def hp():
	hp = float(input("enter the hp :"))
	w = hp * 746
	kw = w * 1000
	a = w / 220 
	print("convert hp to walt : ",w," w")
	print("convert hp to kilowatt : ",kw," amp")
	print("convert hp to amp : ",a," amp")
	

print("watt , kilowatt , amp , hp. ")
	
choice = input("enter the user choice : ")

if choice == 'watt':
	watt()
	
elif choice == 'kilowatt':
	kilowatt()
	
elif choice == 'amp':
	amp()
	
elif choice == 'hp':
	hp()
	
else:
	print("invalid key.")
	
	

'''

output ===

watt , kilowatt , amp , hp.
enter the user choice : amp
enter the amp :456
convert amp to walt :  100320.0  w
convert amp to kilowatt :  100320000.0  amp
convert amp to horsepower :  134.47721179624665  hp


watt , kilowatt , amp , hp.
enter the user choice : hp
enter the hp :8975
convert hp to walt :  6695350.0  w
convert hp to kilowatt :  6695350000.0  amp
convert hp to amp :  30433.409090909092  amp


watt , kilowatt , amp , hp.
enter the user choice : kilowatt
enter the kilowalt :896
convert kilowatt to walt :  0.896  kw
convert kilowatt to amp :  0.004072727272727273  amp
convert kilowatt to horsepower :  0.0012010723860589813  hp


watt , kilowatt , amp , hp.
enter the user choice : watt
enter the watt :7896587496
convert watt to amp :  35893579.52727272  amp
convert watt to horsepower :  35893579.52727272  hp
convert watt to kilowalt :  35893579.52727272  kw




'''