#104.    Find the Product of two Numbers Using Recursion ..??

x= int(input("enter the 1st no:"))
y= int(input("enter the 2nd no."))
def mul(x,y):
    return x*y
mul(x,y)
print("multiplies of two no. ", mul(x,y))

# Find the sum of two Numbers Using Recursion ..??
def sum(x,y):
    return x+y
sum(x,y)
print("sum of two no. ", sum(x,y))

# Find the difference of two Numbers Using Recursion ..??
def diff(x,y):
    return x-y
diff(x,y)
print("diffenrence  of two no. ",diff(x,y))

# Find the division of two Numbers Using Recursion ..??
def div(x,y):
    return x/y
div(x,y)
print("divison of two no. ", div(x,y))

 # Find the integer division  of two Numbers Using Recursion ..??
def int_div(x,y):
    return x//y
int_div(x,y)
print("integer division of two no. ",int_div(x,y))


 # Find the mod of two Numbers Using Recursion ..??
def mod(x,y):
    return x%y
mod(x,y)
print("modulus/ remainder of two no. ", mod(x,y))
