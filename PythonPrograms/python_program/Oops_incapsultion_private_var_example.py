# Oops using class incapcultion  private variable example ..??

class Sample:
	def __init__(self):
		self.__a = 25        # private variable
	
	def display(self):
		print("In display = ",self.__a)
		
obj = Sample()
obj.display()
obj.__a = 50
obj.display()



'''
output ==

In display =  25
In display =  25

'''