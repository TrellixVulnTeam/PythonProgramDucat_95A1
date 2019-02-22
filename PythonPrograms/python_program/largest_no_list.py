#91.  find the second largest number in list...??

list=[]
n= int(input("enter the no of term:"))
for i in range(1,n+1):
     m=int(input("enter the number:"))
     list.append(m)       # add the number in list.
     list.sort()          # list in sequence form (less to greater order)
print("print the second largest number in list:",list[-2])   # find the second largest no of list.
