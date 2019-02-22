for i in range(1,6):#i=1,2
	for j in range(1,6-i):#j=1(1,4)
		print(" ",end="")
	for k in range(1,i+1):#j=1(1,3)
		print("* ",end="")
	print()
for i in range(4,0,-1):#i=1,2
	for j in range(1,6-i):#j=1(1,4)
		print(" ",end="")
	for k in range(1,i+1):#j=1(1,3)
		print("* ",end="")
	print()
	
'''
	*
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''