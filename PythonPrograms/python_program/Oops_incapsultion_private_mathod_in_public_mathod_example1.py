# private mathod using in bonus mathod in the public mathod always in oops same value in the private value in public use mathod...??


class Sample:
	__a = 25
	def example(self):
		print("In example.")
		
obj = Sample()
print(dir(obj))
print(obj._Sample__a)



'''
output ===
directory  obj private vrriable in the public varriale obj  ...=====>>>>>

['_Sample__a', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'example']
 
25


'''