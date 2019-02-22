for i in range(6):
	for j in range(1,i+1):
		if i%2!=0:
			print(1,end="")
		else:
			print(0,end="")
		
	print()


'''
1
00
111
0000
11111

'''


for i in range(6):
	for j in range(1,i+1):
		if i%2==0:
			print(1,end="")
		else:
			print(0,end="")
		
	print()



'''
0
11
000
1111
00000
'''

for i in range(6):
	for j in range(1,i+1):
		if j%2!=0:
			print(1,end="")
		else:
			print(0,end="")
		
	print()
	
	
'''
1
10
101
1010
10101
'''


for i in range(6):
	for j in range(1,i+1):
		if j%2==0:
			print(1,end="")
		else:
			print(0,end="")
		
	print()

	
	
'''
0
01
010
0101
01010
'''





for i in range(5):
	if i < 3:
		for j in range(i+1):
			print(j%2,end='')
	else:
		for j in range(i+1):
			print((j+1)%2,end='')
		
	print()
	
	
	
'''
1
01
010
1010
10101
'''

