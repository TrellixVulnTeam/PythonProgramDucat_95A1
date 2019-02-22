# Program to transpose a matrix using nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)

   
'''
output ==  

X = [[12,7],
    [4 ,5],
    [3 ,8]]

transpose of x =  [12, 4, 3]
				  [7, 5, 8]
				  
'''


# Python Program to Transpose a Matrix  ????

a = [[2,5,9],
	 [4,6,8],
	 [3,1,7]]
	 
t = [[0,0,0],
	 [0,0,0],
	 [0,0,0]]
	 
for i in range(3):
	for j in range(3):
		t[j][i]=a[i][j]
		
for r in t:
	print(r)

	
'''
output == 

a = [[2,5,9],
	 [4,6,8],
	 [3,1,7]]
	 
transpose of a =  [2, 4, 3]
				  [5, 6, 1]
				  [9, 8, 7]

				  
'''
	
	
	