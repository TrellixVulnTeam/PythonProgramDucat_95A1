#18.  inverted star print....triangle..??


n = int(input('Enter no'))                              
for i in range(1,n+1):
        for j in range(i-1,n):
            print('*',end=' ')
        for k in range(1,i+1):
            print(" "*(k), end=' ')
        print()
		
		
		
'''
output === 
Enter no5
* * * * *
* * * *
* * *
* *
*
'''
                                          # or other mathods...??
n = int(input('Enter no'))                 
for i in range(1, n + 1):
    print(' '*(i-1),'*'*(n+1-i))

	
'''
output === 
n=4
****
 ***
  **
   *

'''