#13. Count the Number of Digits in a Number  ..??


n= int(input("enter the no:"))
temp=n
count=0
while n>0:
    digit=n%10
    count=count+1
    n=n//10
print(count)
