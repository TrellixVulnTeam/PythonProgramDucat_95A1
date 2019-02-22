# Oops incapsultion example  string name of mathod ..???

class Human:
	def SayHello(self,name=None):
		if name is not None:
			print("Hello"+" "+name)
		else:
			print("Hello")
			
obj = Human()
obj.SayHello()
obj.SayHello("Sauarbh shukla")




'''
output ===

Hello
Hello Sauarbh shukla

'''