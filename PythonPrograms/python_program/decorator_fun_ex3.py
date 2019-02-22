# decorators  example 2 now no touch decorators now toword the decorators by this moves program in the decorators ..??

def Sample():
	def example():
		print("In example.")
	print("In sample.")
	print(example)
	return example
	
	
b = Sample()
b()
print(b)





'''
output ==

In sample.
<function Sample.<locals>.example at 0x0032A420>
In example.
<function Sample.<locals>.example at 0x0032A420>

'''