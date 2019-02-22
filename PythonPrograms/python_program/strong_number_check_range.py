# strong check numbers in range ...??       ex---- 145 like strong number == 145 = 1!+4!+5! = 1+24+120 == 145 "strong number."
sum=0
m=int(input("Enter a number:"))
for n in range(1,m+1):
	temp=n
	while(n):
		x=1
		f=1
		r=n%10
		while(x<=r):
			f=f*x
			x=x+1
		sum=sum+f
		n=n//10
	
	if(sum==temp):
		
	print("print strong numbers :",sum)
print("count total strong no: = ",c)