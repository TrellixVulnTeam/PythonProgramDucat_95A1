#101.  print the two list and print the its intersection in any list.  ??

   # find the intersection  of two lists..??
list3=[]
list1=[]
list2=[]
n=int(input('enter the no of terms list1:'))
for i in range(1,n+1):
    m= int(input('enter the no:'))
    list1.append(m)
    list1.sort()
x=int(input('enter the no of term list2:'))
for j in range(1,x+1):
    y= int(input('enter the no:'))
    list2.append(y)
    list2.sort()
# print(list1)
# print(list2)
list3=list1+list2           # add list1 and list2 form.
# print(list3)
A=set(list1)              # set list1 change A in asigne same B in asigne list2.>>>
B=set(list2)
D=A.intersection(B)             # print the A intersection B value in D asigne form.>>>
# print(D)
E=list(D)                      # set convert in list form of E.
print(E)
