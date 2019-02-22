for i in range(1,6):#i=1(1,6)
	for j in range(1,i):#j=1(1,1)
		print(" ",end="")
	for j in range(1,i+1):#j=1(1,4)
		print("*",end="")
	for j in range(1,6-i):#j=1(1,3)
		print("    ",end="")
	for j in range(1,i+1):#j=1(1,4)
		print("*",end="")
	print()
for i in range(4,0,-1):
	for j in range(1,i):
		print(" ",end="")
	for j in range(1,i+1):
		print("*",end="")
	for j in range(1,6-i):
		print("    ",end="")
	for j in range(1,i+1):
		print("*",end="")
	print()
'''
*________________*
_**____________**
__***________***
   ****____****
    ********
'''

'''

*                *
 **            **
  ***        ***
   ****    ****
    **********
   ****    ****
  ***        ***
 **            **
*                *

'''