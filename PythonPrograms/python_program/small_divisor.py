#12.  Find the Smallest Divisor of an Integer ..??




list=[]
n= int(input("enter the no of range:"))
for i in range(1,n+1):
    if n%i==0:
      #  print(i)
        list.append(i)
        list.sort()
# print(list)
print(list[0])

# print(list of great number divisor ):
print(list[-1])