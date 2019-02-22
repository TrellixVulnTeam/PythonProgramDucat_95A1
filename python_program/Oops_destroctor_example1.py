#  destrutor of the file values  by oops mathod of class ...???


class Sample:
	def __init__(self):              # constuctor always run in program call or not first call.
		print("Hello Python Web")
		
	def __del__(self):               # disturctor always run in program call or not last call.
		print("Hello Python Local Server.")
		
a = Sample()



'''
output ==
Hello Python Web
Hello Python Local Server.

'''