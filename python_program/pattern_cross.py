for i in range(5):
	for j in range(5):
		if (i+j)%2!=0:
			print(" ",end="")
		else:
			print("*",end="")
	print()
	
	
	
	
'''
* * *
 * *
* * *
 * *
* * *
'''


for i in range(5):
	for j in range(5):
		if (i+j)%2!=0:
			print("*",end="")
		else:
			print(" ",end="")
	print()
	
	
	
'''
 * *
* * *
 * *
* * *
 * *
'''



for i in range(5):
	for j in range(5):
		if (j%2 == 0 and i%2 != 0) or (i%2 == 0 and j%2!=0):
			print(" ",end="")
		else:
			print("*",end="")
	print()
	
	
	
'''
* * *
 * *
* * *
 * *
* * *
'''



for i in range(5):
	for j in range(5):
		if (j%2 == 0 and i%2 != 0) or (i%2 == 0 and j%2!=0):
			print("*",end="")
		else:
			print(" ",end="")
	print()
	
	
'''
 * *
* * *
 * *
* * *
 * *
'''



for i in range(5):
	for j in range(5):
		if (j%2 == 0 or i%2 != 0) and (i%2 == 0 or j%2!=0):
			print("*",end="")
		elif (i%2!=0 )and(j==0 and j==4):
			print("*",end="")
		else:
			print(" ",end="")
	print()
	
	
'''
* * *                          
 * *
* * *
 * *
* * *
'''
