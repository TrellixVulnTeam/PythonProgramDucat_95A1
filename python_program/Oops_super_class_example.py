# super class in heritence used by oops in class ...???

class Sample():
	def display(self):
		print("In Display fuction of the Sample class")
		
class example(Sample):
	def display(self):
		print("In Display function of the example class")
		super().display()
		print("In second class.")
		
x = example()
x.display()


'''
output ===

In Display function of the example class
In Display fuction of the Sample class
In second class.

'''


class Sample():
	def display(self):
		print("In Display fuction of the Sample class")
		
class example(Sample):
	def display(self):
		print("In Display function of the example class")
		print("In second class.")
		
x = example()
x.display()



# if you not call the super class then the program has same function name already call the last function mathod in python overriding mathod.
'''
output ===


In Display fuction of the Sample class
In second class.

'''