# single heritence example using by OOPS class mathod using by def function looking like the .....????

class A:
	def add(self):
		self.a = int(input("enter the number : "))
		self.b = int(input("enter the number : "))
		return self.a + self.b
		
class B(A):
	def sub(self):
		return self.a - self.b
		
obj = B()
add = obj.add()
sub = obj.sub()
print(add)
print(sub)

# single heritence property has class a to add in b . when user run class b then automatic class a run in time .  this type problem 
# solve then we can use user is the single_heritence mathd otherwise a class property extended the class b property .


'''
output == 


enter the number : 5
enter the number : 8
13
-3

'''

class A:
	def add(self):
		print("In add.")
		
class B(A):
	def show(self):
		print("In show.")
		
obj = B()
obj.add()
obj.show()

'''
output ==

In add.
In show.

'''



class A:
	def add(self):
		self.a = input("enter the name : ")
		self.b = input("enter the caste : ")
		
class B(A):
	def show(self):
		print("Full name of candidate : ",self.a+' '+self.b)
		
obj = B()
obj.add()
obj.show()
print(obj.a)
print(obj.b)
print(A())
print(B())


'''
output ==

enter the number : 45
enter the number : 6
51
39
In add.
In show.
enter the name : saurabh
enter the caste : shukla
Full name of candidate :  saurabh shukla
saurabh
shukla
<__main__.A object at 0x00CC0930>      # this one is the class of address .  b in a then b and a class both address has same ..
<__main__.B object at 0x00CC0930>


'''