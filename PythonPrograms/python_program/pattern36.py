for i in range(1,6):#i=2
	for j in range(1,6-i):#(1,4)1 2 3 
		print(" ",end="")
	for j in range(1,i+1):#(1,2)
		print("*",end=" ")
	print()
for i in range(4,0,-1):#i=2
	for j in range(1,6-i):#(1,4)1 2 3 
		print(" ",end="")
	for j in range(1,i+1):#(1,2)
		print("*",end=" ")
	print()

'''
____*
___* *
__* * *
_* * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''
