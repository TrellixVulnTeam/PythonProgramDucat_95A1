#136.       the print remove the same elements in list ..??

list1=[]
list2=[]
list3=[]
n= int(input("enter the no of term :"))
for i in range(1,n+1):
    m = input("enter the word:")
    list1.append(m)
    list1.sort(key=len)
y= int(input("enter the no of term :"))
for j in range(1,y+1):
    z = input("enter the word:")
    list2.append(z)
    list2.sort(key=len)
list3 = list(set(list1+list2))
print(list3)