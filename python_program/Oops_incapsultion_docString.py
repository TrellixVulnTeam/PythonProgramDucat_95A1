# Oops using the doc string in the incapsultion using class ...??

class Sample:
	"This is help."
	def example(self):
		"Hello World "
		print("In example.")
		
obj = Sample()
print(help(obj))
print(dir(obj))
obj.example()





'''
output ===

Help on Sample in module __main__ object:

class Sample(builtins.object)
 |  This is help.
 |
 |  Methods defined here:
 |
 |  example(self)
 |      Hello World
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

None
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'example']
In example.

C:\Users\Saurabh\Desktop\ducat_jan_oops>python Oops_incapsultion_docString.py
Help on Sample in module __main__ object:

class Sample(builtins.object)
 |  This is help.
 |
 |  Methods defined here:
 |
 |  example(self)
 |      Hello World
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

None
In example.

'''