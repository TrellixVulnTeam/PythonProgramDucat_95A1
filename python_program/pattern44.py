num=int(input("Enter the Number of Rows :  "))#5
for i in range(1,num+1):#i=3(1,6)
	for j in range(1,num+1):#j=5(1,6)
		if(i==1):
			print(j,end=" ")
		elif(i==num):
			print(num+1-j,end=" ")
		elif(j==1):
			print(i,end=" ")
		elif(j==num):
			print(num+1-i,end=" ")
		elif(i==j or i+j==num+1):
			if(i<=num/2):#3<=2.5
				print(j,end=" ")
			else:
				print(num+1-j,end=" ")
		else:
			print(" ",end=" ")
	print()
	
	
'''
row==8
1 2 3 4 5 6 7 8
2 2         7 7
3   3     6   6
4     4 5     5
5     5 4     4
6   6     3   3
7 7         2 2
8 7 6 5 4 3 2 1
'''