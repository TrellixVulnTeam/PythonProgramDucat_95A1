# Two pow class in raise error and using iteration mathod of the function value find the all value ...????


class PowTwo:
	'''class to implemented an iteration of the powers of two '''
	
	def __init__(self,max=0):
		self.max = max
		
	def __iter__(self):
		self.n = 0
		return self
	
	def __next__(self):
		if self.n <= self.max:
			result = 2 ** self.n
			self.n += 1
			return result
			
		else:
			raise StopIteration
			
a = PowTwo(4)
for x in a:
	print(x)
	
	
	
	

	
'''
output ==

1
2
4
8
16

'''




class PowTwo:
	'''class to implemented an iteration of the powers of two '''
	
	def __init__(self,max=0):
		self.max = max
		
	def __iter__(self):
		self.n = 0
		return self
	
	def __next__(self):
		if self.n <= self.max:
			result = 2 ** self.n
			self.n += 1
			return result
			
		else:
			raise StopIteration
			
a = PowTwo(5)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))


'''
output ===

1
2
4
8
16
32
Traceback (most recent call last):
  File "Class_TwoPow_in_itration_using_mathod_py_user.py", line 73, in <module>
    print(next(i))
  File "Class_TwoPow_in_itration_using_mathod_py_user.py", line 63, in __next__
    raise StopIteration
StopIteration
StopIteration 

'''