#152.  sum of n power or x numbers series not factorial form :  1+ x**2/2+x**3/3+----

n= int(input("enter the no of term:"))
x=int(input("enter the value:"))
sum = 1
if n==0:
    print("0")
else:
    for i in range(2,n+1):
         #  print(i)
          sum = sum + (x**i)/i        # print the series and calculate the series value..??
    print(sum)