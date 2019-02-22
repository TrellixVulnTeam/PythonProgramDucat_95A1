#151.     print the list value- Swap the First and Last Value of a List.  >>

list1 = []
n= int(input("enter the no of terms:"))
for x in range(1,n+1):
    m= int(input("enter the no:"))
    list1.append(m)
# print(list1)
A=list1[0]          # A in asigne value in list1[0]; after all list1[0] value in list1[-1]; after
                              # value A print in list[-1]
list1[0]=list1[-1]
list1[-1] = A
print(list1)