# temperture calcultor useing by def function ....????

def fharh():
	c = float(input("enter the celcius : "))
	f = (c * (9/5)) + 32
	k = f + 273 
	print("convert the celcius to fhareheiht : ",f,'*f')
	print("convert the celcius to kelvin : ",k,'*k')
	
def cel():
	f = float(input("enter the fhareheiht : "))
	c = (f -32) * (5/9)
	k = f + 273 
	print("convert the fhareheiht to celcius : ",c,'*c')
	print("convert the fhareheiht to kelvin : ",k,'*k')
	
def kel():
	k = float(input("enter the kelvin : "))
	f = (k - 273)
	c = (f -32) * (5/9)
	print("convert the kelvin to fhareheiht : ",f,"*f")
	print("convert the kelvin to celcius : ",c,"*c")
	
	
print("fharh , cel ,kel.")

choice = input("enter the user choice : ")

if choice == 'fharh':
	fharh()
	
elif choice == 'cel':
	cel()
	
elif choice == 'kel':
	kel()
	
else:
	print("invalid key.")
	
	
	
	
'''
output ==

fharh , cel ,kel.
enter the user choice : kel
enter the kelvin : 375
convert the kelvin to fhareheiht :  102.0 *f
convert the kelvin to celcius :  38.88888888888889 *c


fharh , cel ,kel.
enter the user choice : fharh
enter the celcius : 45
convert the celcius to fhareheiht :  113.0 *f
convert the celcius to kelvin :  386.0 *k


fharh , cel ,kel.
enter the user choice : cel
enter the fhareheiht : 456
convert the fhareheiht to celcius :  235.55555555555557 *c
convert the fhareheiht to kelvin :  729.0 *k


'''