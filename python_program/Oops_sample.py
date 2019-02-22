# class_object use to object in system class address ...???

class Sample():
	def add(self):
		self.a = int(input("enter the first number : "))
		self.b = int(input("enter the second number : "))
	def show(self):
		print("sum : ",self.a + self.b)

obj1 = Sample()
obj2 = Sample()
obj1.add()
obj2.add()
obj1.show()
obj2.show()
print(obj1)
print(obj2)


# run program in cmd then python interpeter python + enterkey  +   from file_name import*   (import* means file all part run at this time..)

'''

enter the first number : 5
enter the second number : 9
enter the first number : 6
enter the second number : 2
sum :  14
sum :  8

                                                      OR 
													


>>> import Oops_sample as o
enter the first number : 5
enter the second number : 4
enter the first number : 8
enter the second number : 9
sum :  9
sum :  17


enter the first number : 5
enter the second number : 966
enter the first number : 64
enter the second number : 66
sum :  971
sum :  130
<__main__.Sample object at 0x00C51CD0>
<__main__.Sample object at 0x00C51D10>


>>> from Oops_sample import*
enter the first number : 45
enter the second number : 87
enter the first number : 96
enter the second number : 68
sum :  132
sum :  164
<Oops_sample.Sample object at 0x010B97D0>
<Oops_sample.Sample object at 0x010B9930>
>>> print(obj1)
<Oops_sample.Sample object at 0x010B97D0>
>>> print(obj2)
<Oops_sample.Sample object at 0x010B9930>
>>> print(obj1.a)
45
>>> print(obj2.a)
96
>>> print(obj1.b)
87
>>> print(obj2.b)
68

'''		
