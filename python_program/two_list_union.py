#107.       find the union of two lists..??

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
list3=list1+list2      # add list3 in list1 and  list2.
A= set(list3)           # oprate the set of list(3) remove the commom number print one time.??
# print(A)
B= list(A)            # set in change the list form .??
print(B)


        # other mathod to use the union of the two list values in any list varriable value..>>>


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
A=set(list1)      # list convert in set.
B=set(list2)
C=A.union(B)       # union key in used the value of C.
# print(C)
D=list(C)
print(D)
