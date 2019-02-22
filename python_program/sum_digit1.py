#105.   Find the Sum of Digits in a Number without Recursion.??

l=[]
b=int(input("Enter a number: "))
while(b>0):
    dig=b%10
    l.append(dig)
    b=b//10
print("Sum is:",sum(l))