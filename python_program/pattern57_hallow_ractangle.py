# hallow square input 5 , user by input .....???

size = 5
inner_size = size - 2
print (' *' * size)
for i in range(inner_size):
    print (' *' + '  ' * inner_size + ' *')
print (' *' * size)


'''
 * * * * *
 *       *
 *       *
 *       *
 * * * * *
'''


size= int(input("enter the side value:  === "))
inner_size = size - 2
print (' *' * size)
for i in range(inner_size):
    print (' *' + '  ' * inner_size + ' *')
print (' *' * size)


'''
side == 10
 * * * * * * * * * *
 *                 *
 *                 *
 *                 *
 *                 *
 *                 *
 *                 *
 *                 *
 *                 *
 * * * * * * * * * *
'''


m, n = 10, 10
for i in range(m):
    for j in range(n):
        print('*' if i in [j, m-1] or j == 0 else ' ', end='')
    print()
	
'''
*
**
* *
*  *
*   *
*    *
*     *
*      *
*       *
**********
'''



print("Enter width")
width = int(input())
print("Enter height")
height = int(input())

for i in range(height):
    if i in[0]:
        print("* "*(width))
    elif i in[(height-1)]:
        print("* "*(width))
    else:
        print("*"+"  "*(width-2)+" *")

		
		
#  breath= 5
#  width= 8
'''

* * * * *
*       *
*       *
*       *
*       *
*       *
*       *
* * * * *

'''
