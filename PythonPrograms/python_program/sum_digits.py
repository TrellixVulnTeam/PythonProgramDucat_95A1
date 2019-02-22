num=int(input("Enter the Number :  "))#154
sum=0
while(num!=0):		#154	15		1		0
	r=num%10
	print(r)		#4		5		1
	sum=sum+r		#0+4=4	4+5=9	9+1=10
	num=num//10 	#15		1		0
print("sum = ",sum)
