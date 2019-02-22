
for i in range(5):
	p = 1
	for j in range(5):
	
		if j%2==0:
			print("*",end="")
		else:
			print(p,end="")
			p = p + 1
	print()
	
	
'''
*1*2*
*1*2*
*1*2*
*1*2*
*1*2*
'''