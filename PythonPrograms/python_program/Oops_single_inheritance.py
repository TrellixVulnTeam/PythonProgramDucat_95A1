# single_inheritance.py  by Oops ..??
 

class Sample:
    def show(self):
        print("In Base Class i.e. Sample Class")
class Example(Sample):
	def display(self):
		print("In Derived Class i.e. Example Class")
obj=Example()
obj.display()
obj.show()


'''
output ===


In Derived Class i.e. Example Class
In Base Class i.e. Sample Class

'''