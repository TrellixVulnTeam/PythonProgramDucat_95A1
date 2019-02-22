class Sample:
	def __init__(self):
		print("In Sample Class")
	def display(self):
		sum=self.a+self.b
		print("Sum = ",sum)
class Example(Sample):
	def __init__(self):
		self.a=int(input())
		self.b=int(input())
		super().display()
		super().__init__()
Example()              
