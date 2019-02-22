#14.  Check if a Number is a Palindrome ...???


n= int(input("enter the no:"))
temp=n
k=n
sum=0
while n > 0:
    digit=n%10
    sum=sum*10+digit
    n=n//10
print(sum)
if sum==k:
    print("number is pilendrome.")
else:
    print("number is not pilendrome.")