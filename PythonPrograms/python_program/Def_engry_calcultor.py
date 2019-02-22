# engry calcultor use def function ...???

def jule():
	k = float(input("enter the calory : "))
	j = k / (0.24)
	kj = k / (240)
	print("convert the calory to jule : ",j," jule.")
	print("convert the calory to kilojule : ",kj," k.j.")
	
def kal():
	j = float(input("enter the jule : "))
	k = j * (0.24)
	kj = j * (1000)
	print("convert the jule to calory : ",k," cal.")
	print("convert the jule to kilojule : ",kj," k.j.")
	
def KE():
	m = float(input("enter the mass : "))
	v = float(input("enter the veloity : "))
	KE =  (1/2)* m * v * v
	print("total kinetic engry : ",KE,"  kg * (s**2) / (m**2)")
	
def PE():
	m = float(input("enter the mass : "))
	g = 9.8 
	h = float(input("enter the height : "))
	PE =  m * g * h
	print("total potentical engry : ",PE,"  kg * (m**2) / (s**2)")
	
	
print(" jule , kal , KE ,PE.")

choice = input("enter the user choice : ")

if choice == "jule":
	jule()
	
elif choice == "kal":
	kal()
	
elif choice == "KE":
	KE()
	
elif choice == "PE":
	PE()
	
else:
	print("invalid key.")
	
	
	
'''
output ===

 jule , kal , KE ,PE.
enter the user choice : PE
enter the mass : 5
enter the height : 1
total potentical engry :  49.0   kg * (m**2) / (s**2)


 jule , kal , KE ,PE.
enter the user choice : KE
enter the mass : 5
enter the veloity : 5
total kinetic engry :  62.5   kg * (s**2) / (m**2)


 jule , kal , KE ,PE.
enter the user choice : jule
enter the calory : 45
convert the calory to jule :  187.5  jule.
convert the calory to kilojule :  0.1875  k.j.


 jule , kal , KE ,PE.
enter the user choice : kal
enter the jule : 1
convert the jule to calory :  0.24  cal.
convert the jule to kilojule :  1000.0  k.j.


'''