'''
1*3*5
1*3*5
1*3*5
1*3*5
1*3*5
'''
for i in range(1,6):
	for j in range(1,6):
		if(j%2!=0):
			print(j,end="")
		else:
			print("*",end="")
	print()	