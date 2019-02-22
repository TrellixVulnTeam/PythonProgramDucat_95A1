#16. Read a Number n And Print the Series "1+2+…..+n= " .....???


n= int(input("enter the no of terms:"))
for i in range(1,n+1):
    if i==n:
        print(i)
    else:
        print(i,end="+")