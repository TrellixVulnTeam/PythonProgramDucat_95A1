# private mathod of the private varriable for using the oops in class ..??

b = 45   #  global value in the any where use the fuction in class or other .
class Sample:
	def __init__(self):
		self.__a = 25
		self.b = b
		
	def display(self):
		print("In display : ",self.__a)       #   private variable
		print("In display : ",self.b)         #   public variable
		
		self.__show()
		
	def __show(self):         # private mathod 
		print("In show.")
		
obj = Sample()
obj.display()




'''
output ===

In display :  25
In display :  45
In show.

# show always mathod perform the def function of the using private mathod before display call after the __show  private mathod call it.

'''
	