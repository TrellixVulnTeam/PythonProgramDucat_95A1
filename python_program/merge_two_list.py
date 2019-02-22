#158.  print the two list and merge it and after the list sort. >>
                              # putting the value of the list in users. >>
list1=[4,5,6,8,75,98,108]
list2 =[45,52,2,3,6,11,13]
list=list1+list2
list.sort()
print(list)

                       # another form in list input the user combined and sort it .>>
                            # input the value from user and combined it in list form. >>
list=[]
list1=[]
list2=[]
n=int(input("enter the no of term in 1st list:"))
for i in range(1,n+1):
    a= int(input("enter the no:"))
    list1.append(a)                                      # add a value in list1.
# print(list1)
m=int(input("enter the no of term in 2nd list:"))
for j in range(1,m+1):
    b= int(input("enter the no:"))                       # add b value in list2.
    list2.append(b)
# print(list2)
list=list1+list2                                  # list1 and list2 are merge in list [].>>
list.sort()
print(list)