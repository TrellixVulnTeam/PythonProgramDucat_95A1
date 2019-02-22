#32. Find Those Numbers which are Divisible by 7 and Multiple of 5 in a Given Range of Numbers ..??



n= int(input("enter the lower limit:"))
m= int(input("enter the upper limit:"))
for i in range(n,m+1):
    if (i%7==0 or i%5==0):
        print(i)
