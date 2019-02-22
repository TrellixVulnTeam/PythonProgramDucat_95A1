#134.       Remove the Duplicate Items from a List .

list1=[]
list2=[]
list3=[]
n= int(input("enter the no of term."))
for i in range(1,n+1):
    m =int(input("enter the no:"))
    list1.append(m)
    list1.sort()
y= int(input("enter the no of term."))
for j in range(1,y+1):
    z=int(input("enter the no:"))
    list2.append(z)
    list2.sort()
list3 = list(set(list1+list2))     # change set to list again print list.
print(list3)