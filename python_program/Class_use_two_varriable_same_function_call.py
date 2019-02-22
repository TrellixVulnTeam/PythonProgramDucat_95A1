# Class is used to double varriable of the code : ...??

class Sample:
	def example(q):
		print("In example",q)
a = Sample()
a.example()
b = Sample()
b.example()

'''
output == 

In example <__main__.Sample object at 0x00AD15B0>
In example <__main__.Sample object at 0x00AD1670>

In example
In example

'''


class Sample():
	def add(self):
		self.a = input("enter the name : ")
	def show(self):
		print("your name : ",self.a)
		
obj = Sample()
obj1 = Sample()
obj.add()
obj1.add()
obj.show()
obj1.show()


'''
output ==

In example <__main__.Sample object at 0x00AD15B0>
In example <__main__.Sample object at 0x00AD1670>
enter the name : saurabh
enter the name : shivam
your name :  saurabh
your name :  shivam

'''