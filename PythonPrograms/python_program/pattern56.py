# diagram of stars on grade type ...???

for i in range(1,6+1):
	for j in range(1,6+1):
		if (i==1):
			print("*",end=" ")
		elif (j==1):
			print("*",end=" ")
		elif (i==6):
			print("*",end=" ")
		elif (j==6):
			print("*",end=" ")
		elif (i==j or i+j==6+1):
			if (i<=(6+1)/2):
				print("*",end=" ")
			else:
				print("*",end=" ")
		else:
			print(" ",end=" ")
	print()
	
	
	
'''
* * * * * *
* *     * *
*   * *   *
*   * *   *
* *     * *
* * * * * *

'''

num= int(input("enter the value of row :  == "))
for i in range(1,num+1):
	for j in range(1,num+1):
		if (i==1):
			print("*",end=" ")
		elif (j==1):
			print("*",end=" ")
		elif (i==num):
			print("*",end=" ")
		elif (j==num):
			print("*",end=" ")
		elif (i==j or i+j==num+1):
			if (i<=(num+1)/2):
				print("*",end=" ")
			else:
				print("*",end=" ")
		else:
			print(" ",end=" ")
	print()
	
	
	
# when num   ==  10 :

'''
* * * * * * * * * *
* *             * *
*   *         *   *
*     *     *     *
*       * *       *
*       * *       *
*     *     *     *
*   *         *   *
* *             * *
* * * * * * * * * *
'''


num= int(input("enter the value of row :  == "))
for i in range(1,num+1):
	for j in range(1,num+1):
		if (i==1):
			print(" * ",end="   ")
		elif (j==1):
			print(" * ",end="   ")
		elif (i==num):
			print(" * ",end="   ")
		elif (j==num):
			print(" * ",end="   ")
		elif (i==j or i+j==num+1):
			if (i<=(num+1)/2):
				print(" * ",end="   ")
			else:
				print(" * ",end="   ")
		else:
			print("   ",end="   ")
	print()
	
	
	
# user input the value of rows == 10:

'''
 *     *     *     *     *     *     *     *     *     *
 *     *                                         *     *
 *           *                             *           *
 *                 *                 *                 *
 *                       *     *                       *
 *                       *     *                       *
 *                 *                 *                 *
 *           *                             *           *
 *     *                                         *     *
 *     *     *     *     *     *     *     *     *     *

'''





num= int(input("enter the value of row :  == "))
for i in range(1,num+1):
	for j in range(1,num+1):
		if (i==1):
			print("***",end="	")
		elif (j==1):
			print("***",end="	")
		elif (i==num):
			print("***",end="	")
		elif (j==num):
			print("***",end="	")
		elif (i==j or i+j==num+1):
			if (i<=(num+1)/2):
				print("***",end="	")
			else:
				print("***",end="	")
		else:
			print("   ",end="	")
	print()
	
	
	
'''
 ***     ***     ***     ***     ***     ***     ***
 ***     ***                             ***     ***
 ***             ***             ***             ***
 ***                     ***                     ***
 ***             ***             ***             ***
 ***     ***                             ***     ***
 ***     ***     ***     ***     ***     ***     ***
 
'''