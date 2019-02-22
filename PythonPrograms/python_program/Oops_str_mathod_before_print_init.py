# consturctor in the init function work like to first always str_mathod  work as (def __str__(self):) ==>>>  work first the init def..

# the string mothod always work before init function . (str mathod ====>>>       def __str__(self):  )    class address is self.


class Sample():
	def __init__(self):
		self.name = input("enter the your name : ")
		
	def __str__(self):
		return self.name
	
	def example(self):
		print("IN EXAMPLE.")
			
obj = Sample()
print(obj)


'''
output ==
enter the your name : ram
ram

'''

# string value user can drops of the class paratehese code any string has input so output has their types ...


class Sample():
	def __init__(self,name):
		self.name = name
		
	def __str__(self):
		return self.name
	
	def example(self):
		print("IN EXAMPLE.")
			
obj = Sample("Shyam kumar sharma.")
print(obj)


'''
output ==

enter the your name : ram
ram
Shyam kumar sharma.

'''