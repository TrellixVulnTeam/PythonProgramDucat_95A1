#116.  # LCM (least common factor) of the two numbers ..>>
n=int(input("enter the 1st num."))
m=int(input("enter the 2nd num."))
a=m
b=n
while m!=n:
    if m>n:
         m=m-n
    else:
         n=n-m
print("HCF =",m)
LCM = (a*b)/m
LCM = int(LCM)
print("LCM =",LCM)
