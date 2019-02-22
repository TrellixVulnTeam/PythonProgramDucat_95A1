# Python Add Digits of Number  ???

n= int(input("enter the input by user: "))
sum=0
while n > 0:
	digit = n%10
	sum=sum+digit
	n= n//10
print("sum of digit : ",sum)

'''
output ==

enter the input by user: 7896
sum of digit :  30
'''