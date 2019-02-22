# python work on the overadding concept but not work in overloding  concept given example..??

# same class work on the same def funtion name but python work on always the line by line code so work on the always last def mathod has same name.

class Sample():
	def A(self,name="ram"):
		self.name = name
		print("your name : ",self.name)
	def A(self,name="ram",age=0):                   # if you initization of the value then given always u intization but not u given def then change of value intization.  by deafault given u prevoius set value.. 
		self.name = name
		self.age = age
		print("your name : ",self.name)
		print("your age : ",self.age)
a = Sample()
a.A("shyam",78)


'''

your name :  ram
your age :  20


if 1 argument pass in the class example then we can right this form ..???
only pass name but not age pass so givin the error of the code in python interpeter.
TypeError: A() missing 1 required positional argument: 'age'

'''


class Sample():
	def __init__(self,name):
		self.name = name
		
	def __str__(self):
		return self.name
		
	def __str__(self):
		return "hello ducat."
		
a = Sample("ram")
print(a)


'''
output ==
hello ducat.
# always print beacuse the str has same function name but always python read lne by line so print last same function mathod.


'''
