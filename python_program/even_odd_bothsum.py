n= int(input("put the user choice numbers:"))
sum=0
for i in range(n):
	print("all number print in user range :",i)
	sum= sum+i
print("sum of all numbers:",sum)


m= int(input("users choice print even numbers range:"))

sum1=0
for j in range(m):
	if j%2==0:
		print("all even numbers in users range:",j)
		sum1= sum1+j
print("sum of all even numbers:",sum1)


p= int(input("users choice print odd numbers range:"))

sum2=0	
for k in range(p):
	if k%2!=0:
		print("all odd numbers in users range :",k)
		sum2= sum2+k
print("sum of all odd numbers:",sum2)



