#  currency calcultor by use def function  ......?????


# rupee (₹) = dollaor ($) , rupee = euro (€) , rupee = yen( ¥ ) , rupee = kuwatidinner ( k.d. / kwd / د.ك) 


def rupees():
	print("rupees change in all currency : ")
	rupees = float(input("enter the rupee format :"))
	dollar = rupees / 70
	euro = rupees / 80
	yen = rupees / 1.6
	kuwatidinner = rupees / 231
	print("dollar: ",str(dollaor)+' $')
	print("euro: ",str(euro)+' €')
	print("yen: ",str(yen)+' ¥' )
	print("kuwatidinner: ",str(kuwatidinner)+' K.D. (kuwatidinner)')

def dollar():
	print("dollaor convert in rupees : ")
	dollar = float(input("enter the dollar format :"))
	rupees = dollar * 70
	return(str(rupees)+chr(8377))

def euro():
	print("euro convert in rupees : ")
	euro =float(input("enter the euro format : " ))
	rupees = euro * 80
	return(str(rupees)+chr(8377))
	
def yen():
	print("yen convert in rupees : ")
	yen = float(input("enter the yen format : "))
	rupees = yen * 0.63
	return(str(rupees)+chr(8377))
	
def kuwatidinner():
	print("kuwatidinner convert in rupees : ")
	kuwatidinner = float(input("enter the biggest currency in world kuwatidinner format : "))
	rupees = kuwatidinner * 231
	return(str(rupees)+chr(8377))
	

print("rupees , dollar , euro , yen , kuwatidinner ")

choice = input("enter the choice of user find and search currency : ")

if choice == 'rupees':
	rupees()
	
elif choice == 'dollar':
	print(dollar())
	
elif choice == 'euro':
	print(euro())
	
elif choice == 'yen':
	print(yen())
	
elif choice == 'kuwatidinner':
	print(kuwatidinner())
	
else:
	print("ivalid key.")
	
	
	
	
'''
output ===

rupees , dollar , euro , yen , kuwatidinner
enter the choice of user find and search currency : rupees
rupees change in all currency :
enter the rupee format :800
dollaor:  11.428571428571429 $
euro:  10.0 €
yen:  500.0 ¥
kuwatidinner:  3.463203463203463 K.D. (kuwatidinner)


rupees , dollar , euro , yen , kuwatidinner
enter the choice of user find and search currency : yen
yen convert in rupees :
enter the yen format : 800
504.0₹


rupees , dollar , euro , yen , kuwatidinner
enter the choice of user find and search currency : dollar
dollaor convert in rupees :
enter the dollar format :800
56000.0₹


'''