#125.    Compute a Polynomial Equation given that the Coefficients of the Polynomial are stored in a List
list=[]
n= int(input("enter the no of terms:"))
x= int(input("enter the no of terms:"))
for i in range(0,n):
   #  print(i)
    m= int(input("enter the no:"))
    list.append(m)
sum = 0
for i in range(len(list)):
    sum = sum + list[i]*(x ** ((len(list)-1)-i))       # calculate the value of x in panomial cacul...>>
print(sum)