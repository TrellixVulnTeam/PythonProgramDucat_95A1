#108.      find the sum of the x power series . 1+x**2/2!+x**3/3!+---- ??

def fact(n):
    fact = 1
    while n > 0:
        fact *= n
        n = n - 1
    return fact
list=[]
n=int(input("enter the number of term :"))
x=int(input("enter the value of x:"))
sum=1
for i in range (1,n+1):
    sum = sum + (x**(i+1))/fact(i+1)
print(sum)