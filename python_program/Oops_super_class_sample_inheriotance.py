# sample_inheriotance.py     by Oops ..??
# super_class inheritence ..py  ..???


class Sample:
    def get(self):
        self.a=int(input("Enter Value of a "))
        self.b=int(input("Enter Value of b "))
    def display(self):
        self.sum=self.a+self.b
        print("Sum = ",self.sum)
    def get(self):
        self.a=int(input("Enter a "))
        self.b=int(input("Enter b "))
    
class Example(Sample):
	def get(self):
		print("Welcome")
		super().get()
		super().display()
		print("Bye")
obj=Example()
obj.get()



'''
output ===

Welcome
Enter a 5
Enter b 9
Sum =  14
Bye


'''