#124.   print the Put Even and Odd elements in a List into Two Different Lists ..>>

list1=[]                # print even no.
list2=[]                # print odd no.
n=int(input("enter the no of terms:"))
for i in range(1,n+1):
    m =int(input("enter the no:"))
    if m%2==0:                        # even no print from list1 and after add this value in list1.
       list1.append(m)

    else:
        list2.append(m)
print(list1)
print(list2)