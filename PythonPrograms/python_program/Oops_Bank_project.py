# from the bank project By oops using class mathod in def fuction also use ...???

# run program then python write in interpeture on the cmd .  after (From Oops_Bank_project import* )    import*  ==  all in bank project of def.


import random as rd
class Bank():
	def add(self):
		self.name = input("enter the name : ")
		self.age = int(input("enter the age : "))
		self.mob = int(input("enter the mobile number : "))
		self.address = input("enter the address : ")
		self.pincode = int(input("enter the pincode : "))
		self.account_number = rd.randrange(1111111,9999999)
		# self.account_number = rd.randrange(1111111,9999999)
		self.balance = int(input("enter the ammount : "))
		
	def deposite(self,ammount = 0):
		self.balance = self.balance + ammount
		# self.balance+=ammount
		print("your new balance : ",self.balance)
		
	def withdrawl(self,ammount = 0):
		if (ammount <= self.balance):
			self.balance = self.balance - ammount
			# self.balance-=ammount
			print("remaning balance : ",self.balance)
		else:
			print("low balance : ",self.balance)
			
	def show_detail(self):
		print("name : ",self.name)
		print("age : ",self.age)
		print("mobile number : ",self.mob)
		print("address : ",self.address)
		print("pincode : ",self.pincode)
		print("account_number : ",self.account_number)
		print("current balance : ",self.balance)
		
		
		
a = Bank()
a.add() 
a.withdrawl(2000)
a.deposite(5000)
a.show_detail()





'''
output ==

enter the name : ram
enter the age : 25
enter the mobile number : 9864996586
enter the address : noida25
enter the pincode : 205016
enter the ammount : 5000
name :  ram
age :  25
mobile number :  9864996586
address :  noida25
pincode :  205016
account_number :  2401074
current balance :  5000



enter the name : shyam
enter the age : 52
enter the mobile number : 7896857496
enter the address : kanpur
enter the pincode : 2018016
enter the ammount : 45000
name :  shyam
age :  52
mobile number :  7896857496
address :  kanpur
pincode :  2018016
account_number :  5643217
current balance :  45000
remaning balance :  43000
your new balance :  48000


>>> from Oops_Bank_project import*
enter the name : ram
enter the age : 56
enter the mobile number : 7896857496
enter the address : noida56
enter the pincode : 2019201
enter the ammount : 450000
remaning balance :  448000
your new balance :  453000
name :  ram
age :  56
mobile number :  7896857496
address :  noida56
pincode :  2019201
account_number :  5345435
current balance :  453000

python interpeture in cmd print   ===>>>>    python + enter .

>>> from Oops_Bank_project import*
enter the name : ram
enter the age : 54
enter the mobile number : 7893456322
enter the address : kanpur
enter the pincode : 54212156
enter the ammount : 148931
remaning balance :  146931
your new balance :  151931
name :  ram
age :  54
mobile number :  7893456322
address :  kanpur
pincode :  54212156
account_number :  8788266
current balance :  151931
>>> a=Bank()
>>> a.add()
enter the name : shyam
enter the age : 58
enter the mobile number : 7896587462
enter the address : noida
enter the pincode : 201524
enter the ammount : 895647
>>> a.deposite(45000)
your new balance :  940647

>>> a.withdrawl(20000)
remaning balance :  920647
>>> a.show_detail()
name :  shyam
age :  58
mobile number :  7896587462
address :  noida
pincode :  201524
account_number :  2575464
current balance :  920647

'''






