#145.  sort list according to the len of list element ..??
           # print any value in string type . any number or name both in string form..>>
list=[]
n = int(input("enter the no of term:"))
for i in range(1,n+1):
    m = input("enter the no:")      # m value in string type not any integer type.
    list.append(m)
list.sort(key=len)                    # list of key sort in length . >>
print(list)
