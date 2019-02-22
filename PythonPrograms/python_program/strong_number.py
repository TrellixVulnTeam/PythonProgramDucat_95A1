# strong check numbers in range ...??

sum=0
n=int(input("Enter a number:"))
temp=n
while(n):
    x=1
    f=1
    r=num%10
    while(x<=r):
        f=f*x
        x=x+1
    sum=sum+f
    n=n//10
if(sum==temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")