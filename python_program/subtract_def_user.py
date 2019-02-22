# def subtact values user choice in order : ??

# output  ==  (5,6,8,9,70)    ===>>>>      5-6-8-9-70  == -88

def sub(*a):
	sub = a[0]
	for x in range(1,len(a)):
		sub = sub - a[x]
	print("total sub : ",sub)
	
sub(253,7,8,9,6,9,10,90,123)

'''
output ===

total sub :  -9

'''
