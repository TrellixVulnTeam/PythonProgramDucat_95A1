# reverse numbers check in range ..??
m= int(input("enter the no:"))
for n in range(m+1):
	temp = n
	sum=0
	while n>0:
		rem = n%10
		sum = sum*10+rem
		n=n//10
	print("reverse numbers = ",sum)

