# constructer is also pre define constouctor  ( like that : def __init__(): )  ==>>>>

class Sample():
	def __init__(self):
		print("INIT.")
	def example(self):
		print("IN EXAMPLE.")
		
obj = Sample()
obj1 = Sample()
obj2 = Sample()
print(obj,obj1,obj2)


'''
output==
INIT
INIT
INIT

'''


class Sample():
	def __init__(self):
		print("INIT.")
	def example(self):
		print("IN EXAMPLE.")
		

obj1 = Sample()
print(Sample())

obj2 = Sample()
obj2.example()

'''
output ==

INIT.
INIT.
<__main__.Sample object at 0x033F0930>
INIT.
IN EXAMPLE.

'''


