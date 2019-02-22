# Oops using class incapcultion  public variable example ..??


class Sample:
	def __init__(self):
		self.a = 25      # public varriable
	
	def display(self):
		print("In display = ",self.a)
		
obj = Sample()
obj.display()
obj.a = 50
obj.display()



'''
output ==
In display = 25 
In display = 50

'''
	