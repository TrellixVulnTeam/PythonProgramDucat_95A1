# main example of decorator  in python code ...??

# decorator ***

def Sample(fun):
	def example():
		fun()
		print("In example")
	print("In sample")
	return example

@ Sample     

				# this is decorator syntax   @ funtion name ..     ****   add = Sample(add)	

def add():
	print("In add")
	
add()




'''

output ===

In sample
In add
In example

'''

	