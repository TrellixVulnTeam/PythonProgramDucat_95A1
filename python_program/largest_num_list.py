#99.   find the largest number in list..??

list=[]
n= int(input("enter the no of term:"))
for i in range(1,n+1):
     m=int(input("enter the number:"))
     list.append(m)
     list.sort()
print(max(list))