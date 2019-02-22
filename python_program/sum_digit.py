#11.  Find the Sum of Digits in a Number ..??


n= int(input("enter the no of term:"))
temp=n
sum=0
while n>0:
     digit=temp%10
     sum=sum+digit
     temp=temp//10
print(sum)
