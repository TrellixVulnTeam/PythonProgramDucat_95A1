#95.    Find the Factorial of a Number Using Recursion . ??

def fact(n):
    if(n <= 1):
        return 1
    else:
        return(n*fact(n-1))     # n multiply the no of n-1 elements no which n is not equal to 1 and less than .
n = int(input("Enter number:"))
print("Fact:",fact(n))