#  data calcultor use by def function ...????

def GB():
	gb = float(input("enter the gb : "))
	mb = gb * (1024)
	byte = gb * (1024 * 1024)
	bit = gb * (1024 * 1024 * 8)
	print("enter the gb to mb : ",mb)
	print("enter the gb to byte : ",byte)
	print("enter the gb to bit : ",bit)
	
	
def MB():
	mb = float(input("enter the mb : "))
	gb = mb / (1024)
	byte = mb * 1024
	bit = mb * 1024 * 8
	print("enter the mb to gb : ",gb)
	print("enter the mb to byte : ",byte)
	print("enter the mb to bit : ",bit)
	
	
	
def Byte():
	byte = float(input("enter the byte : "))
	gb = byte / (1024 * 1024)
	mb = byte / 1024 
	bit = byte * 8
	print("enter the byte to gb : ",gb)
	print("enter the byte to mb : ",mb)
	print("enter the byte to bit : ",bit)
	
	
def Bit():
	bit = float(input("enter the bit : "))
	gb = bit / (1024 * 1024 * 1024 )
	mb = bit / (1024 * 1024)
	byte = bit / 8
	print("enter the bit to gb : ",gb)
	print("enter the bit to mb : ",mb)
	print("enter the bit to byte : ",byte)
	
	
print("GB , MB , Byte , Bit. ")

choice = input("enter the user choice : ")

if choice == 'MB':
	MB()
	
elif choice == 'GB':
	GB()
	
elif choice == 'Byte':
	Byte()
	
elif choice == 'Bit':
	Bit()
	
else:
	print("invalid key.")
	
	
	
'''

output ===

GB , MB , Byte , Bit.
enter the user choice : GB
enter the gb : 4
enter the gb to mb :  4096.0
enter the gb to byte :  4194304.0
enter the gb to bit :  33554432.0


GB , MB , Byte , Bit.
enter the user choice : MB
enter the mb : 5698
enter the mb to gb :  5.564453125
enter the mb to byte :  5834752.0
enter the mb to bit :  46678016.0


GB , MB , Byte , Bit.
enter the user choice : Bit
enter the bit : 459876953235323
enter the bit to gb :  428293.788093443
enter the bit to mb :  438572839.00768566
enter the bit to byte :  57484619154415.375


GB , MB , Byte , Bit.
enter the user choice : Byte
enter the byte : 45987654134325
enter the byte to gb :  43857244.61967945
enter the byte to mb :  44909818490.55176
enter the byte to bit :  367901233074600.0



'''