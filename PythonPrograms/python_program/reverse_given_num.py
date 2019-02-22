#5.  Reverse a Given Number ..??


n = int(input("enter the number:"))
temp = n
sum = 0
while n>0:
    digit = n%10
    sum = sum*10 + digit
    n = n//10
print("reverse of the number:",sum)