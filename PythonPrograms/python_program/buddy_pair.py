# buddy pairs ===>>>  48 prime divisiable == 1+2+3+4+6+8+12+24 ==76            =========     (75 + 1) == 76
# 75 prime diviasiable == 1+3+5+15+25 == 49                     ===========      (48 + 1) == 49





n= int(input("enter the value of n: "))
m= int(input("enter the value of m: "))

sum = 0
i = 1
while i < n:
#for i in range(1,n):
	if n%i==0:
		#print(i)	
		sum=sum+i
	i = i + 1
print(sum)
a=sum
		
sum1=0	
j = 1
while j < m:	
#for j in range(1,m+1):
	if m%j==0 and m!=j:
		#print(j)
		sum1=sum1+j
	j = j + 1
print(sum1)
b=sum1
if b == n+1  and a == m+1:
	print("the number pairs is buddy pair.")
else:
	print("the number pairs is not buddy pair.")
	
	
	
	
	                                    OR    (using for loop ) ......????
										



										
n= int(input("enter the value of n: "))
m= int(input("enter the value of m: "))

sum = 0
for i in range(1,n):
	if n%i==0:
		#print(i)	
		sum=sum+i
print(sum)
a=sum
		
sum1=0	
#for j in range(1,m+1):
	if m%j==0 and m!=j:
		#print(j)
		sum1=sum1+j
print(sum1)
b=sum1
if b == n+1  and a == m+1:
	print("the number pairs is buddy pair.")
else:
	print("the number pairs is not buddy pair.")
	