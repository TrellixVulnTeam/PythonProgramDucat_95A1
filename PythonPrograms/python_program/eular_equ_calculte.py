#62.    compute the eular's equ. and calculate them....???



def fact(n):                  # define the function of n  used for factorial used .??
    fact = 1
    while n > 0:
        fact =fact* n
        n = n - 1
    return fact
n=int(input("enter the number of term :"))
x=int(input("enter the value of x:"))
sum=1
for i in range (1,n+1):
    sum = sum  +  (x**i) / fact(i)     # used the eular's rule in series form.
print(sum)