# decorators  ==>>>   function functionalltity extend but touch and call always in called decorators ...??

# decorators  in python code example .

def inc(x):
	return x+1
	
def dec(x):
	return x-1
	
def operate(func,x):
	return func(x)
	
b = operate(inc,5)
print(b)



'''
output ==
6
'''


def inc(x):
	return x+1
	
def dec(x):
	return x-1
	
def operate(func,x):
	return func(x)
	
b = operate(dec,5)
print(b)



'''
output ==
4
'''