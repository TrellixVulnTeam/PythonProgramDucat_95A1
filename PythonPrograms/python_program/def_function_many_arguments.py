# def function with many arguments ..??

def add(*a):        # many value we can used the *()astrick of a   @ == (*a)
	print("A: ",a)
add(1,5,7,8,9,6,7,8)


'''
output ===

A:  (1, 5, 7, 8, 9, 6, 7, 8)

'''

def add(*a):             # many value we can used the *()astrick of a   @ == (*a)
	s = 0
	for x in a:
		s = s + x
	print("ans: ",s)
add(4,5,2,9)

	
'''
output ===

ans:  20

'''
	
def add(*a):        # many value we can used the *()astrick of a   @ == (*a)
	print("A: ",sum(a))
add(1,5,7,8,9,6,7,8)


'''
output ==

A:  51

'''