#65.  cosine series print and sumation of its:


def fact(n):        # define the function of n  used for factorial used .??
    fact = 1
    while n > 0:
        fact*=n
        n = n - 1
    return fact
n=int(input("enter the number of term :"))
x=int(input("enter the value of x:"))
sum=1
for i in range (1,n+1):
    sum = sum + ((((-1)**i)) * (x**(2*i))) / fact(2*i)  # cosine series formula in fact values.
print(sum)