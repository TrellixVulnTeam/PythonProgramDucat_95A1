# single inheritence to next example ...???

class Sample():
	def add(self):
		self.a = int(input("enter the first no : "))
		self.b = int(input("enter the second no : "))
		
class example(Sample):
	def display(self):
		sum = self.a + self.b
		sub = self.a - self.b
		mul = self.a * self.b
		div = self.a / self.b
		print("sum of two numbers : ",sum)
		print("subtact of two numbers : ",sub)
		print("multiple of two numbers : ",mul)
		print("division of two numbers : ",div)
		
obj = example()
obj.add()
obj.display()




'''

output ===

enter the first no : 5
enter the second no : 8
sum of two numbers :  13
subtact of two numbers :  -3
multiple of two numbers :  40
division of two numbers :  0.625

'''