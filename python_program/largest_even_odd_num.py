#30. Print Largest Even and Largest Odd Number in a List ..??


list1=[]
list2=[]
n= int(input("enter the no of terms:"))
for i in range(1,n+1):
    m= int(input("enter the no:"))
    if (m%2==0):
        list1.append(m)
        list1.sort()
    else:
        list2.append(m)
        list2.sort()
print("largest even no: =",list1[-1])
print("largest odd no: =",list2[-1])
