# speed calcultor used def function .....???

def kmh():
	cm = float(input("enter the cm : "))
	sec = float(input("enter the sec : "))
	m = cm / (10**2)
	km = cm / (10**5)
	feet = cm / (30.5)
	miles = cm / (160934)
	min = sec / 60
	hour = sec / 3600
	print((km /hour)," km / hour")
	
	
def metersec():
	cm = float(input("enter the cm : "))
	sec = float(input("enter the sec : "))
	m = cm / (10**2)
	km = cm / (10**5)
	feet = cm / (30.5)
	miles = cm / (160934)
	min = sec / 60
	hour = sec / 3600
	print((m /sec)," m / sec")

	
def cmsec():
	cm = float(input("enter the cm : "))
	sec = float(input("enter the sec : "))
	m = cm / (10**2)
	km = cm / (10**5)
	feet = cm / (30.5)
	miles = cm / (160934)
	min = sec / 60
	hour = sec / 3600
	print((cm /sec)," cm / sec")

	
def feetsec():
	cm = float(input("enter the cm : "))
	sec = float(input("enter the sec : "))
	m = cm / (10**2)
	km = cm / (10**5)
	feet = cm / (30.5)
	miles = cm / (160934)
	min = sec / 60
	hour = sec / 3600
	print((feet / sec)," feet / sec")
	

def milesh():
	cm = float(input("enter the cm : "))
	sec = float(input("enter the sec : "))
	m = cm / (10**2)
	km = cm / (10**5)
	feet = cm / (30.5)
	miles = cm / (160934)
	min = sec / 60
	hour = sec / 3600
	print((miles /hour)," miles / hour")
		
	
print("kmh , metersec , cmsec , feetsec , milesh .")

choice = input("enter the user choice : ")

if choice == 'kmh':
	kmh()
	
elif choice == 'metersec':
	metersec()
	
elif choice == 'cmsec':
	cmsec()
	
elif choice == 'feetsec':
	feetsec()
	
elif choice == 'milesh':
	milesh()
	
else:
	print("invalid key .")
	
	
	
'''
output ===


kmh , metersec , cmsec , feetsec , milesh .
enter the user choice : cmsec
enter the cm : 45
enter the sec : 89
0.5056179775280899  cm / sec


kmh , metersec , cmsec , feetsec , milesh .
enter the user choice : feetsec
enter the cm : 89
enter the sec : 96
0.03039617486338798  feet / sec


kmh , metersec , cmsec , feetsec , milesh .
enter the user choice : milesh
enter the cm : 986
enter the sec : 89
0.2478229961811409  miles / hour


kmh , metersec , cmsec , feetsec , milesh .
enter the user choice : kmh
enter the cm : 9865
enter the sec : 4589
0.07738940945739813  km / hour


'''