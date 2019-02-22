# OOps using init _ sample using class ...????

class ABCD:
	def add(self):
		self.a = int(input("Enter First Number: "))
		self.b = int(input("Enter Second Number: "))
	def display(self):
		print('sum : ',self.a+self.b)

obj=ABCD()
obj1=ABCD()
obj.add()
obj1.add()
obj.display()		
obj1.display()



'''
output ===

Enter First Number: 5
Enter Second Number: 89
Enter First Number: 5
Enter Second Number: 52
sum :  94
sum :  57

'''