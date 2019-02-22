#   chirsmas  tree  by stars ...*****.

'''
####################
or input value==
n=1
 *
***

or input value==
n=2
  *
 ***
  *
  *
*****
or input value==
n=3
   *
  ***
   *
   *
 *****
   *
   *
   *
*******
##################

'''

n= int(input("enter the number of rows :"))
p = 3
k = n
for i in range(1,n+1):
	for j in range(1,i+1):
		print(' '*n+'*'+' '*n)
	k = k - 1
	print(' '*k+'*'*p+' '*k)
	p = p + 2
print()

