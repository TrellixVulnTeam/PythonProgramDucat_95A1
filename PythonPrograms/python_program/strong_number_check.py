# strong check numbers in range ...??       ex---- 145 like strong number == 145 = 1!+4!+5! = 1+24+120 == 145 "strong number."

sum=0
n=int(input("Enter a number:"))
temp=n
while(n):
    x=1
    f=1
    r=n%10
    while(x<=r):
        f=f*x
        x=x+1
    sum=sum+f
    n=n//10
if(sum==temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")