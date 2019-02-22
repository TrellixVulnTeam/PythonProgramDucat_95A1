#142.  find the programm  to Search the Number of Times a Particular Number Occurs in a List . ??

list=[]
n= int(input("enter the no of term:"))
x=int(input("enter the search no:"))
for i in range(1,n+1):
     m=int(input("enter the number:"))
     list.append(m)
count=0
for k in list:
    if k==x:
       count=count+1
print(count)