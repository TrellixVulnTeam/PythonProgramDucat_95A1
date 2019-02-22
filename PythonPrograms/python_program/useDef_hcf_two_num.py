#114.     hcf of two no. of the Number Recursively ..??
x= int(input("enter the 1st no."))
y= int(input("enter the 2nd no."))
def hcf(x,y):
    if (x==0):
        return y
    if (y==0):
        return x
    return hcf(y,x%y)
print(hcf(x,y))


 # lcm of the two number recursively ..??

x= int(input("enter the 1st no."))
y= int(input("enter the 2nd no."))
def gcd(x,y):
    if (x==0):
        return y
    if (y==0):
        return x
    return gcd(y,x%y)
print(gcd(x,y))
LCM = (x*y)//gcd(x,y)       # integer division of the values.
# LCM = int(LCM)         # diviser of integer then not change lcm in int . but division of no so change in int form.
print("two no of lcm =",LCM)
