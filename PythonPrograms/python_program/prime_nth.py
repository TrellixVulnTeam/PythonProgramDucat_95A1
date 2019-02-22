c=0
num=2
n=int(input("Enter the Value of N to get Nth Prime Number  : "))
while(c<n):
	f=0
	for i in range(2,int(num**.5)+1):
		if(num%i==0):
			f=1
			break
	if(f==0):
		c=c+1 
	num=num+1
print("\nNth Prime Number is ",num-1," if value of n is",n)