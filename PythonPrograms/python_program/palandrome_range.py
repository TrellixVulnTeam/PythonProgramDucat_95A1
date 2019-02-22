# palandrome numbers check in range ..??
c=0
m= int(input("enter the no:"))
for n in range(m+1):
	temp = n
	sum=0
	while n>0:
		rem = n%10
		sum = sum*10+rem
		n=n//10
	if temp==sum:
		c=c+1
		print("palandrome numbers = ",sum)
print("count the palandrome number in range : = ",c)
	