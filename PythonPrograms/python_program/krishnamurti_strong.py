a= int(input("enter the no :"))
sum=0
while(a!=0):
	b=a%10
	fact=1
	while b!=0:
		fact=fact*b
		b=b-1
	sum=sum+fact
	a=a//10
print(sum)