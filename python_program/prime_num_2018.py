n = int(input('Enter the number'))

for i in range(2,n+1):
	flag = 0
	j = 2
	while j < i//2+1:
		if i % j == 0:
			flag = 1
			break
		j = j + 1
	if flag == 0:
		print(i)
		