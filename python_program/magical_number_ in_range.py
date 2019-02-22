# magical numbers ...??
# 1729 == digit sperates.. 1+7+2+9=19  digits sum after its reverse then multiply sum of digit is equal input number...
# 1729 == digits 1+7+2+9 = 19 -->>  reverse 91  ====>>>  19*91 == 1729 "it is a magical numbers"

list=[]
p= int(input("enter the no:"))
c=0
for n in range(1,p+1):
	sum=0
	t=n
	sum1=0
	
	while n!=0:
		rem= n%10
		sum=sum+rem
		n=n//10
	'''
	print("digits sum input by user choice number :: == ",sum)
	'''
	s=sum
		
	while sum!=0:    
		rem_digit=sum%10  
		sum1=sum1*10+rem_digit 
		sum=sum//10
	'''
	print("digits reverse numbers:: == ",sum1)
	'''
	a=sum1
	m = (s * a)      # print(m) digit sum and its reverse both multiply choce of user value in range.. 
	'''
	print("this is multiply digit sum and her reverse:: == ",m)
    '''
	if (t==m):
		'''
		print("input by user choice number is magical == ",t)
		'''
		list.append(t)
		c=c+1
print("total count magical number in range :: == ",c)

print(list)
