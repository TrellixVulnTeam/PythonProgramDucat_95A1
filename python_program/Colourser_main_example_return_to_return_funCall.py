# Clourser main example in python code ...??

def make_multiplier_of(n):
	def multiplier(x):
		return x*n
	return multiplier
	
times3 = make_multiplier_of(5)
times5 = make_multiplier_of(7)
print(times3(9))
print(times5(10))
print(times3(times5(2)))




'''
output ==

5*9 == 45
7*10 == 70
5*7*2 == 70

'''