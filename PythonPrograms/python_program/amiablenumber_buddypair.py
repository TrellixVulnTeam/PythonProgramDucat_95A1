# buddy pair / amiable number ----->>>>   a pair of numbers her spratly prime diviable fact and after sum the value equal to oposite number 
# like that 220,284
# 220 === 1,2,4,5,10,11,22,44,55,110 ==   1+2+4+5+10+11+22+44+55+110  == 284
# 284 === 1,2,4,71,142 ==  1+2+4+71+142  == 220         # important that the number can not include that numbers also ..??


n= int(input("input the no: "))
m= int(input("input the no: "))
t=n
x=m
sum=0
sum1=0
for i in range(1,n):
	if n%i==0 :
		'''
		print(i)
		'''
		sum=sum+i
		'''
		print("sum of first no factor :: == ",sum)
		'''
		a=sum
for j in range(1,m):
	if (m%j==0):
		'''
		print(j)
		'''
		sum1=sum1+j
		'''
		print("sum of second no factor :: == ",sum1)
		'''
		b=sum1
if (t==b and x==a):
	print("number of pair is amiable / buddy pair .")
else:
	print("number of pair is not amiable / buddy pair .")