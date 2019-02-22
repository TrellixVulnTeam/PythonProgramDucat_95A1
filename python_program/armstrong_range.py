# Python Program to Find Armstrong Number in an Interval  ????

m= int(input("enter the number "))
c=0
for n in range(1,m+1):
	temp=n
	sum=0
	while n > 0:
		digit= n%10
		sum = sum + digit**3
		n=n//10
	# print(sum)
	if temp == sum:
		print("armstrong number : ",sum)
		c=c+1
print("total armstrong number ",c)

'''
output == 
enter the number 100000
armstrong number :  1
armstrong number :  153
armstrong number :  370
armstrong number :  371
armstrong number :  407
total armstrong number  5

'''