# satr make pattern ...

for i in range(1,6):
	for j in range(5-i):
		print(" ",end="")
	if (i==5):
		for q in range(i):
			print("* ",end="")
		break
	for j in range(1):
		print("*",end="")
	for j in range(1,(i-1)*2):
		print(" ",end="")
	if (i>1):
		for j in range(1):
			print("*",end="")
	print()
	
	
	
'''
    *
   * *
  *   *
 *     *
* * * * *
'''

# if condotion me yadi print * ke baad space nhi diya to kuch asa shape banega...??

'''
         *
       *    *
     *        *
   *            *
 *  *  *  *  *
'''