# Python Program to Multiply Two Matrices   ????


l = [[1,2,3],
	 [2,3,4],
	 [3,4,5]]

m = [[3,4,5],
	 [5,6,7],
	 [6,7,8]]

for i in range(3):     
	for j in range(len(l)):    
		sum = 0           
		for k in range(len(m)):   
			sum=sum + l[i][k] * m[k][j]
		print(sum,end=" ")
	print()

	

''' 
output == 

	l = [[1,2,3],  
	     [2,3,4],  
		 [3,4,5]]  
		 
	m = [[3,4,5],
	     [5,6,7],
		 [6,7,8]]
		 
		 
output ====  ***********
	l*m =   31 37 43   *
			45 54 63   *
			59 71 83   *
	   ====  ***********
'''
