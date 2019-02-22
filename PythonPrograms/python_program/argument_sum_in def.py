 # user add of def used function to add all argument :  ??
 
def add(*a):
	print("total sum of a : ",sum(a))
add(5,7,78,89,56,65,36,25,4)


'''
output == 

total sum of a :  365

'''

def add(*a):
	sum = 0
	for x in a:
		sum = sum + x
	print("total sum of a : ",sum)
add(5,7,78,89,56,65,36,25,4)

'''
output ==

total sum of a :  365

'''