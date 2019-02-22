#8. Print all Numbers in a Range Divisible by a Given Number...??


n =int(input("enter the no of term using the range value."))
m = int(input("enter the divisible given the no."))
for i in range(1,n+1):
    if i % m==0:
        print(i)

