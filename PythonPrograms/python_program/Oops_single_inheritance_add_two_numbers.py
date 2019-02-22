# single_inheritance_add_two_numbers.py   using Oops _ class ...???


class Sample:
	def get(self):
		print(self)
		self.a=int(input())
		self.b=int(input())
class Example(Sample):
	def display(self):
		print(self)
		sum=self.a+self.b
		print("Sum  = ",sum)
obj=Example()
obj.get()
obj.display()


'''
output ===

<__main__.Example object at 0x00CB1590>
5
6
<__main__.Example object at 0x00CB1590>
Sum  =  11

'''
