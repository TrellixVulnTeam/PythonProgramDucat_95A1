#117.   find the programm List of Words and Return the Length of the Longest One.  >>>

list1 =['shyam','gopi','raju','ghanshyam','babloo','sita','chuve']
list1.sort(key=len)
print(list1)
print(list1[-1])

        # another mathod used for string length return value is longest one...>>

list1=[]
n=int(input("enter the no of terms:"))
for x in range(1,n+1):
    m=input("enter the value:")
    list1.append(m)
    list1.sort(key=len)
print(list1)
print(list1[-1])