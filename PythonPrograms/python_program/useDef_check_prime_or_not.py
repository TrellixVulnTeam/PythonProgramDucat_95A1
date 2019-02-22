#90.    Find if a Number is Prime or Not Prime Using Recursion ..??

n= int(input("enter the prime no:"))

def check(n):
    k = 0
    isprime = True          # true key is prime no  search and check both .??
    for i in range(2, (n // 2) + 1):
        if (n % i == 0):
            k = k + 1
        if (k <= 0):
            return isprime
    else:
       isprime = False
    return isprime
check(n)
# print(check(n))
if check(n)==True:
    print("prime no")
else:
    print(" not prime no")