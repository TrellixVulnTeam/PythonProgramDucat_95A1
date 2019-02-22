#  class demo is pass and got address form ..??

class Sample():     # class Sample:
	pass
obj = Sample()
print(obj)



'''

output ==  Given output of address of class in hexadecimal : ....

<__main__.Sample object at 0x002E0CF0>

'''


class Sample():     # class Sample:
	def example(q):                            # def function minimum 1 argument store in parasentenses..
		print("In example ")
a = Sample()
a.example()

'''
output ==
<__main__.Sample object at 0x00DEDC10>
In example
'''


class Sample():     # class Sample:
	def example(q):                            # def function minimum 1 argument store in parasentenses..
		print("In example ")
a = Sample()
a.example()
print(type(a))
print(type(Sample))


'''

output ===

<__main__.Sample object at 0x0143DC10>
In example
In example
<class '__main__.Sample'>
<class 'type'>

'''



class Sample():     # class Sample:
	def example(q):                            # def function minimum 1 argument store in parasentenses..
		print("In example ")
a = Sample()
a.example()
b = Sample()
b.example()



'''
output ==

<__main__.Sample object at 0x0129DC10>
In example
In example
<class '__main__.Sample'>
<class 'type'>
In example
In example


'''