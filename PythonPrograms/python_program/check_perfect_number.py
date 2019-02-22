#34.  Check if a Number is a Perfect Number  ..??
# perfect sum factor sum as same as user input number but not include this number .
# like that ==  6   , factor = 1,2,3,6(* not include this condition so.)   ===>>>>
# 6 = 1+2+3    (6 is perfect number.)	



n= int(input("enter the no:"))
k=n
sum=0
for i in range(1,n+1):
    if (n%i==0 and n!=i):
        # print(i)
        sum=sum+i
print(sum)
if (k==sum):
    print("perfect no.")
else:
    print("not perfect no.")
