#1. combination of three number if two no are same then print combination of numbers..??


n = int(input("enter the no:"))
m = int(input("enter the no:"))
o = int(input("enter the no:"))
for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(1,o+1):
            if (i==j or j==k or k==i):
                print(i,j,k)
