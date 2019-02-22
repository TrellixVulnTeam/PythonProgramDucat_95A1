for i in range(5):
	for j in range(5):
		if i%2==0 and j%2==0:
			print("1",end="")
		elif i%2!=0 and j%2!=0:
			print("1",end="")
		elif i%2!=0 and j%2==0:
			print("0",end="")
		elif i%2==0 and j%2!=0:
			print("0",end="")
		else:
			print()
	print()
	
	
'''
10101
01010
10101
01010
10101
'''