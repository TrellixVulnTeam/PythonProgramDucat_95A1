#20. print the identity matrix ..??


row,col=2,2
for row in range(2):
    for col in range(2):
         if (row==col):
              print("1",end=' ')
         else:
             print("0",end=" ")
    print()
	
'''
output ===

1 0
0 1
'''	


                                # or other mathods....??


n=int(input("enter the row:"))
m=int(input("enter the col:"))
row,col=n,m
for row in range(n):
    for col in range(m):
        if (row == col):
            print("1", end=' ')
        else:
            print("0", end=" ")
    print()


'''
output ===

enter the row:5
enter the col:5
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1

'''