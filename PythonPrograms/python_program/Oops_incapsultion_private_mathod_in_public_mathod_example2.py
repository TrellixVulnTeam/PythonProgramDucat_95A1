# private mathod using in bonus mathod in the public mathod always in oops using to change value in the private value in public use mathod...??



class Sample:
	__a = 25
	def example(self):
		print("In example.",self.__a)
		
obj = Sample()
obj.example()
obj._Sample__a = 50
obj.example()



'''
output ===

In example. 25
In example. 50


'''