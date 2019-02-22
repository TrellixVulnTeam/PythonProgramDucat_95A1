# all error handle to file handling to all data programm in handle to ingore that : 

import sys
a=['a',0,2]
for entry in a:
	try:
		print("the entry is : ",entry)
		r= 1/(int(entry))
		print(r)
	except:
		print("oops!",sys.exc_info()[1],"occured.")
		
		
'''
output ==

sys.exc_info()[list of any index : ]


the entry is :  a
oops! invalid literal for int() with base 10: 'a' occured.
the entry is :  0
oops! division by zero occured.
the entry is :  2
0.5


'''