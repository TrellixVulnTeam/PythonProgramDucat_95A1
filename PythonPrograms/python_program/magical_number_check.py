# magical numbers ...??
# 1729 == digit sperates.. 1+7+2+9=19  digits sum after its reverse then multiply sum of digit is equal input number...
# 1729 == digits 1+7+2+9 = 19 -->>  reverse 91  ====>>>  19*91 == 1729 "it is a magical numbers"

n= int(input("enter the no:"))
sum=0
t=n
sum1=0


while n!=0:
	rem= n%10
	sum=sum+rem
	n=n//10
print("digits sum input by user choice number :: == ",sum)
s=sum
# print(s)
	
while sum!=0:    
	rem_digit=sum%10  
	sum1=sum1*10+rem_digit 
	sum=sum//10
print("digits reverse numbers:: == ",sum1)
a=sum1
# print(a)
m=s*a
print("this is multiply digit sum and her reverse:: == ",m)

if (t==m):
	print("input by user choice number is magical . ")
else:
	print("input by user choice number is not magical .")