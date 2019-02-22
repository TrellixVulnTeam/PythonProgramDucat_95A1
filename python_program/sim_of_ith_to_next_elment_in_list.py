#122.   Find the Cumulative Sum of a List where the ith Element is the Sum of the First i+1 Elements From The Original List

list1=[]
list2=[]
n =int(input('enter the no of term:'))
for x in range(1,n+1):
    m = int(input("enter the no:"))
    list1.append(m)
print(list1)      # input value by user add in list form.
sum=0
for y in list1:
    # print(y)
    sum = sum+y
   #  print(sum)
    list2.append(sum)      # print the sum of the input values in any list2 is print .
print(list2)