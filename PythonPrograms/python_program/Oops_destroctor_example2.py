#  destrutor of the file values  by oops mathod of class ...???


class Sample:
	def __init__(self):              # constuctor always run in program call or not first call.
		self.a = 25
		
	def __del__(self):               # disturctor always run in program call or not last call.
		del self.a
		print("Hello Python Local Server.")
		print("Deleted")
		
obj = Sample()
print(obj.a)


'''
output ====
25
Hello Python Local Server.
Deleted

'''


class Sample:
	def __init__(self):              # constuctor always run in program call or not first call.
		self.a = 25
		
	def __del__(self):               # disturctor always run in program call or not last call.
		del self.a
		print("Deleted")
		
obj = Sample()
print(obj.a)



'''
output ===

25
Deleted

'''