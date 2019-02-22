# init_in_inheritence  using bye Oops ..???

class Outer:
	def display(self):
		print(self)
		print("In display function of Outer class")
		class Local:
			def show(self):
				print("In Show function of Local Class")
		AB=Local()
		print(AB)
		AB.show()
	class Inner:
		def print_value(self):
			print("In Print_Value function of Inner Class")
obj=Outer()
obj.display()
print(dir(obj))
a=Outer.Inner()
#	a.show()
a.print_value()



'''

output ===

<__main__.Outer object at 0x01721870>
In display function of Outer class
<__main__.Outer.display.<locals>.Local object at 0x01740870>
In Show function of Local Class
['Inner', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'display']
In Print_Value function of Inner Class


'''