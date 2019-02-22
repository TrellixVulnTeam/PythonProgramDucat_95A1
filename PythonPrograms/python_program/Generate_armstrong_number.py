# Python Generate Armstrong Numbers  ???
# armstrong numbers check in range ..??


c=0
m= int(input("enter the no:"))
for n in range(m+1):
	temp = n
	sum=0
	while n>0:
		rem = n%10
		sum = sum+rem**3
		n=n//10
	if temp==sum:
		c=c+1
		print("armstrong numbers = ",sum)
print("count the armstrong number in range : = ",c)
		
		
'''
output ===

enter the no:1000
armstrong numbers =  0
armstrong numbers =  1
armstrong numbers =  153
armstrong numbers =  370
armstrong numbers =  371
armstrong numbers =  407
count the armstrong number in range : =  6

'''
	