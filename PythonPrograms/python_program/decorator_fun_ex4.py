# decorators  example 2 now no touch decorators now toword the decorators by this moves program in the decorators ..??

def Sample(fun):
	def example():
		fun()
		print("In example")
	print("In sample")
	
	return example

def add():
	print("In add")
	
b = Sample(add)
b()



'''
output ==

In sample
In add
In example

'''