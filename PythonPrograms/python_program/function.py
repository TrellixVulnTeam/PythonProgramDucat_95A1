def add():
	a=12
	def sample():
		nonlocal a
		a=9
		print(a)
	sample()
	print(a)	
add()