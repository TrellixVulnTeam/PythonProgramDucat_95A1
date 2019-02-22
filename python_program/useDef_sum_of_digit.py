#155.     the Sum of the Digits of the Number Recursively ...???

n= int(input("enter the no:"))
def sum_digit(n):
    if(n==0):
        return 0
    else:
        return n%10 + sum_digit(n//10)
print(sum_digit(n))
