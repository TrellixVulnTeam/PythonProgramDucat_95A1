#150.   sum of the 1+1/2+1/3+1/4 ------ numbers .

n=int(input("enter the number:"))
sum=0
for i in range (1,n+1):
   # print(i)
    sum=sum+(1/i)      # because not print 1/n series number not print(i).
print(" 1/n numbers sum = ",sum)