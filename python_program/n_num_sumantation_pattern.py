#17. Read a Number n and Print the Natural Numbers Summation Pattern ..??



n= int(input("enter the no of term:"))
for i in range(1,n+1):
    for j in range(1,i+1):
             if j==i:
                print(j, end='')
             else:
                 print(j, end="+")
    print("")

	
'''
output ==

enter the no of term:6
1
1+2
1+2+3
1+2+3+4
1+2+3+4+5
1+2+3+4+5+6

'''