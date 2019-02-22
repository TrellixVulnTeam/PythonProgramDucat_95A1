#81.    Determine Whether a Given Number is Even or Odd Recursively .??

def check(n):
    if(n < 2):
        return ( n % 2 == 0)
    return(check (n-2))
n = int(input("enter the no:"))
if (check(n)== True):
     print(' number of even no.')
else:
    print(' number of odd no.')