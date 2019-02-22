#29. Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List ..??


list=[]
n= int(input("enter the list no of terms:"))
for i in range(1,n+1):
    m= int(input("enter the no in add list :"))
    list.append(m)
# print(list)
sum=0
for x in list:
   # print(x)
   if (x>0 and x%2==0 ):
       print("positive even no:",x)
   elif (x<0):
      sum=sum+x
   else:
       print("positive odd no:",x)
print("sum of the negative no:",sum)


'''
output ===

enter the list no of terms:9
enter the no in add list :-4
enter the no in add list :5
enter the no in add list :8
enter the no in add list :-9
enter the no in add list :-78
enter the no in add list :-6
enter the no in add list :45
enter the no in add list :2
enter the no in add list :3
positive odd no: 5
positive even no: 8
positive odd no: 45
positive even no: 2
positive odd no: 3
sum of the negative no: -97

'''