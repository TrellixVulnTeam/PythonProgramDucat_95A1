#96.     find the factorial of a number without recursion.??

n = int(input("enter the no of term:"))
i=1
fact =1
while i < n+1:
    fact = fact*i
    i=i+1
print(fact)