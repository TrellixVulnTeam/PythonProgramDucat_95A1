# multilevel program example in oops class....??


class Base():
	def get(self):
		self.a = [25,2,45,1,452,125,785,215,12,12,2,3,5,51,2]
		
class Derived1(Base):
	def display(self):
		print(self.a)
		
class Derived2(Derived1):
	def sort(self):
		self.a.sort()
		
class Derived3(Derived2):
	def reverse(self):
		self.a.reverse()
		
obj = Derived3()
obj.get()
print("Original list is : ")
obj.display()
obj.sort()
print("Sorted list is : ")
obj.display()
obj.reverse()
print("Reversed list is : ")
obj.display()



'''

output ==

Original list is :
[25, 2, 45, 1, 452, 125, 785, 215, 12, 12, 2, 3, 5, 51, 2]
Sorted list is :
[1, 2, 2, 2, 3, 5, 12, 12, 25, 45, 51, 125, 215, 452, 785]
Reversed list is :
[785, 452, 215, 125, 51, 45, 25, 12, 12, 5, 3, 2, 2, 2, 1]

'''