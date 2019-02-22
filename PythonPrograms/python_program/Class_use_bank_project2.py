# Class use the bank project 2 ...???

class Customer():
	"""A customer of ABC Bank with a checking account. Customers have the
	following properties:

	Attributes:
	name: A string representing the customer's name.
	balance: A float tracking the current balance of the customer's account.
	"""

	def __init__(self, name):
		"""Return a Customer object whose name is *name*.""" 
		name = input("enter the name of customer : ")
		self.name = name

	def set_balance(self, balance=0.0):
		"""Set the customer's starting balance."""
        self.balance = balance

	def withdraw(self, amount):
		"""Return the balance remaining after withdrawing *amount*
		dollars."""
		if amount > self.balance:
			raise RuntimeError('Amount greater than available balance.')
		self.balance = self.balance - amount
        return self.balance

	def deposit(self, amount):
		"""Return the balance remaining after depositing *amount*
		dollars."""
		self.balance = self.balance + amount
		return self.balance
		
		
a = Customer()
b = a.deposit(balance=500)
print(b)

		

 
