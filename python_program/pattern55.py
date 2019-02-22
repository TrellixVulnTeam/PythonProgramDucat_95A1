# pattern in number form ....??

num = int(input("enter the no of row by user. == "))       # input of row == 7
for i in range(1,num+1):
	for j in range(1,num+1):
		if (i==1):
			print(j,end=" ")
		elif (j==1):
			print(i,end=" ")
		elif (i==num):
			print(num+1-j,end=" ")
		elif (j==num):
			print(num+1-i,end=" ")
		elif (i==j or i+j==num+1):
			if (i<=(num+1)/2):
				print(j,end=" ")
			else:
				print(num+1-j,end=" ")
		else:
			print(" ",end=" ")
	print()
	
	
	


# if  input of rows ===  7: 	
'''
1 2 3 4 5 6 7
2 2       6 6
3   3   5   5
4     4     4
5   5   3   3
6 6       2 2
7 6 5 4 3 2 1

'''



for i in range(1,6+1):
	for j in range(1,6+1):
		if (i==1):
			print(j,end=" ")
		elif (j==1):
			print(i,end=" ")
		elif (i==6):
			print(6+1-j,end=" ")
		elif (j==6):
			print(6+1-i,end=" ")
		elif (i==j or i+j==6+1):
			if (i<=(6+1)/2):
				print(j,end=" ")
			else:
				print(6+1-j,end=" ")
		else:
			print(" ",end=" ")
	print()
	
	
'''
1 2 3 4 5 6
2 2     5 5
3   3 4   4
4   4 3   3
5 5     2 2
6 5 4 3 2 1

'''


