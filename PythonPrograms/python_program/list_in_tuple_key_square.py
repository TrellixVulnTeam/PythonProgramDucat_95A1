#157.    Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number:..??



list=[]
n= int(input("enter the no of lower limit:"))
m= int(input("enter the no of upper limit:"))
x=n
for x in range(n,m+1):
    list1=(x,x**2)      # tuple form in used in list1...??
    list.append(list1)       # list value add in list values.
print(list)