#98.     Find the Fibonacci Series without Using Recursion

n = int(input("enter the no of term:"))
a = 0
b = 1
print(a)
print(b)
sum=1
for i in range(2,n):
    c= a+b
    a = b
    b = c
    print(c)
    sum= sum+c
print("fibonacci series:",sum)