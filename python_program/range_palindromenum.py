c=0
for a in range(1,1000):
	r=0
	t=a
	while a!=0:
		b=a%10
		r=r*10+b
		a=a//10
	if(t==r):
		print(t,"y")
		c=c+1
print("total palindrome number count :",c)