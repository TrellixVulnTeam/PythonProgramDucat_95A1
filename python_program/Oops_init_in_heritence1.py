# inheritence init _ function class base using the OOps file ..???


class Sample:
    def __init__(self):
        print("In Base Class i.e. Sample Class")
class Example:
	def __init__(self):
		print("In Derived Class i.e. Example Class")
class Example2(Sample,Example):
	def __init__(self):
		print("In Example2 class")
		super().__init__()
		print("Hello World")
obj=Example2()



'''
output ===
In Base Class i.e. Sample Class
In Derived Class i.e. Example Class
In Example2 class
Hello World

'''