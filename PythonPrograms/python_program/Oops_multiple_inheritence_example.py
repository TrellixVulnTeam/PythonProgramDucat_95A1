# multiple inhertence example using oops class ...???

# note ==>>   user complete choice of base1 and base2 all put input numbers other wise one and second no put add other intize number 
# then program run and given result  other wise error output given number.  

class Base1():
	def get1(self):
		print("enter the two number of the class base1 : ")
		self.a = int(input("enter the first num : "))
		self.b = int(input("enter the second num : "))

class Base2():
	def get2(self):
		print("enter the two number of the class base2 : ")
		self.c = int(input("enter the first num : "))
		self.d = int(input("enter the second num : "))
		
class Derived(Base1,Base2):
	def display(self):
		sum = self.a + self.b + self.c + self.d
		print("sum of base1 and base2 : ",sum)
		
obj = Derived()
obj.get1()
obj.get2()
obj.display()



'''
1. user input base1 input but not given the base2 input then program given error value of the numbers ...
value error..
2. user choice to both function name same then print input first in the class inhertience call always first one ..
# derived(base1,base2)
call always base1   when the user name same of the names .. [ (def name ),(def name) , two calss def then always call up the first in 
derived function .]  ==>>   def name call of the first one in the paratenses  

enter the two number of the class base1 :
enter the first num : 5
enter the second num : 8
enter the two number of the class base2 :
enter the first num : 9
enter the second num : 3
sum of base1 and base2 :  25


enter the two number of the class base1 :
enter the first num : 2124
enter the second num : 12
enter the two number of the class base2 :
enter the first num : 54332
enter the second num : 543
sum of base1 and base2 :  57011

'''
'''

class Base1():
	def get(self):
		print("enter the two number of the class base1 : ")
		self.a = int(input("enter the first num : "))
		self.b = int(input("enter the second num : "))

class Base2():
	def get(self):
		print("enter the two number of the class base2 : ")
		self.c = int(input("enter the first num : "))
		self.d = int(input("enter the second num : "))
		
class Derived(Base1,Base2):
	def display(self):
		sum = self.a + self.b + self.c + self.d
		print("sum of base1 and base2 : ",sum)
		
obj = Derived()
obj.get()
obj.get()
obj.display()



output ===

enter the two number of the class base1 :
enter the first num : 65659
enter the second num : 5542
enter the two number of the class base1 :
enter the first num : 6312
enter the second num : 652
Traceback (most recent call last):
  File "Oops_multiple_inheritence_example.py", line 68, in <module>
    obj.display()
  File "Oops_multiple_inheritence_example.py", line 62, in display
    sum = self.a + self.b + self.c + self.d
AttributeError: 'Derived' object has no attribute 'c'


'''

# other wise same def function so python use overrding mathod so use to last mathod inbuilt  already in program ..