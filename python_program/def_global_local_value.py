#  gloabal keys  used the value is global (keys ==(a,b,n))    likes ===>>>>  global  a,b,n   use this type..??

a = 45   # global value 
# (after comes in local value becuse def used the local value first in program ..???)
def sample():
	a = 121     # (local keys ) 
# 	preorty first in global value because def used first to local value after global value...??
	print("in sample : ",a)
sample()
print("in main value :",a)

'''
output ==

in sample :  121
in main value : 45

'''

a = 125
def sample():
	print("in sample : ",a)
sample()
print("in main value :",a)


'''
output ===

in sample :  125
in main value : 125

'''