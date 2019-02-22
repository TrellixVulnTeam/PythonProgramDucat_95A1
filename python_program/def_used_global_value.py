# global varriable  used by indef users.??

def sample():
	global a,b,s
	a = int(input("a : " ))
	b = int(input("b : " ))
	s = a + b
	print("total : ",s)
# global s
sample()
print(s + 2)

# note ===>>>   single s has global key only ...
'''
output ===

a : 5
b : 9
total :  14
16

'''