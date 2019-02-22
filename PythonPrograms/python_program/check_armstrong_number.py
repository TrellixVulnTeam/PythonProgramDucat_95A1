#33. Check if a Number is an Armstrong Number ..??


n= int(input("enter the no :"))
temp=n
k=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10
print(sum)
if (sum == k):
    print("it is a armstrong number.")
else:
    print("it is not armstrong number.")