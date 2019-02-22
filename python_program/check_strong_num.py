#35. Python Program to Check if a Number is a Strong Number ..??
         # strong no : the sum of the factorials of the digits is equal to the numbers


n=int(input("enter the strong number:"))
k=n
sum=0
while n > 0:
    i=1
    f=1
    r=n%10
    while i<=r:
        f=f*i
        i=i+1
    sum=sum+f
    n//=10
print(sum)
if sum==k:
    print("no is strong :")
else:
    print("no is not strong :")