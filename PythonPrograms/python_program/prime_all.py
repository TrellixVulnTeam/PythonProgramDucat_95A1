from math import *
c,d=0,0
n=int(input("Enter Range : "))
for num in range(2,n):
	f=0
	for i in range(2,int(sqrt(num))+1):
		if(num%i==0):
			f=1
			d+=1
			print("Not prime: ",num,end="\t")
			break
	if(f==0):
		print("Prime : ",num,end="\t")
		c=c+1#c=1
print("\nTotal Prime Numbers = ",c,"\nTotal Not prime :",d)
	