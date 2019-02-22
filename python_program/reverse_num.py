#141.  find the reverse numbers:....???
n=int(input("enter the value:"))
sum=0
while n>0:
    r=n%10
    sum=sum*10+r
    n//=10
print(sum)
