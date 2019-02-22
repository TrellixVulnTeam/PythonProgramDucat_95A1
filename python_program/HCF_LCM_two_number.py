# Python Find HCF & LCM  ????

n = int(input("enter the number : "))
m = int(input("enter the number : "))
while m != n:
	if m > n:
		m = m - n
	else:
		n = n - m
	hcf = m
print("hcf : ",hcf)

'''
output == 

enter the number : 34
enter the number : 12
hcf :  2

'''

# Python Find HCF & LCM  ????


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

'''
output ===

enter the number : 20
enter the number : 40
hcf :  20
enter the 1st num.20
enter the 2nd num.40
HCF = 20
LCM = 40

'''



