#106.   Find the Sum of Elements in a List Recursively..??

def sum_arr(arr,size):
   if (size == 0):
     return 0
   else:
     return arr[size-1] + sum_arr(arr,size-1)
n=int(input("Enter the number of elements for list:"))
a=[]
for i in range(0,n):
    element=int(input("Enter element:"))
    a.append(element)
print("The list is:",a)
b=sum_arr(a,n)
print("Sum of items in list:",b)