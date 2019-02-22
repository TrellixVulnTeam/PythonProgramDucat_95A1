#112.  GCD (highest common factor) of the two numbers ..>>


n=int(input("enter the 1st num."))
m=int(input("enter the 2nd num."))
while m!=n:
    if m>n:
        m=m-n
    else:
        n=n-m
print("print the GCD numbers of two num. :",m)