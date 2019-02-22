list=[]
n=int(input("enter the value:"))
i=1
for i in range(1,n+1):

    if n%i==0:                   # condition the no of hers factors .....??
        list.append(i)
        i=i+1
print(max(list))                          # min / max value find out numbers of integer value..??
print(min(list))