#use class salary of empolyee in use of def function ...???

n = int(input("user choice depend how many entry got it in company "))
class Emp_Salary():
	def name(self):
		self.name = input("enter the name of empolyee : ")
	def father_name(self):
		self.father_name = input("enter the father_name of empolyee : ")
	def company(self):
		self.company_name = input("enter the company_name : ")
		self.company_address = input("enter the company_address : ")
	def company_salary(self):
		self.basicsalary = int(input("enter the basic salary : "))
		hra = self.basicsalary * (0.06)
		da = self.basicsalary * (0.05)
		ta = self.basicsalary * (0.06)
		fund  = self.basicsalary * (0.07)
		self.salary = self.basicsalary + hra + da + ta - fund 
	def show(self):
		print("the empolyee name : ",self.name)
		print("the empolyee father_name : ",self.father_name)
		print("the company name : ",self.company_name)
		print("the company_address : ",self.company_address)
		print("total salary of empolyee hand to hand Givin by company : ",round(self.salary,2))


for i in range(n):		
	a = Emp_Salary()
	a.name()
	a.father_name()
	a.company()
	a.company_salary()
	a.show()





'''
output ==

user choice depend how many entry got it in company 2
enter the name of empolyee : ram
enter the father_name of empolyee : shyam
enter the company_name : hcl
enter the company_address : noida62
enter the basic salary : 12000
the empolyee name :  ram
the empolyee father_name :  shyam
the company name :  hcl
the company_address :  noida62
total salary of empolyee hand to hand Givin by company :  13200.0
enter the name of empolyee : shyam
enter the father_name of empolyee : hardev pasad
enter the company_name : tcs
enter the company_address : newdelhi
enter the basic salary : 12500
the empolyee name :  shyam
the empolyee father_name :  hardev pasad
the company name :  tcs
the company_address :  newdelhi
total salary of empolyee hand to hand Givin by company :  13750.0

'''




























