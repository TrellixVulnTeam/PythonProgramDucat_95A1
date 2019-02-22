# Python Program to Find Sum of Natural Numbers Using Recursion  using for loop ????

def sum(m):
	sum=0
	
	for i in range(1,m+1):
		sum= sum + i
	return sum

m= int(input("enter the range : "))
print("total of terms sum = ",sum(m))

'''
output == 

enter the range : 12
total of terms sum =  78
'''


# Python Program to Find Sum of Natural Numbers Using Recursion  using while loop ????

def sum(n):
	sum=0
	i=1
	while n >= i:
		sum = sum + i
		i=i+1
	return sum
	
n= int(input("enter the no of range : "))
print("total of terms sum = ",sum(n))

'''
output == 

enter the no of range : 15
total of terms sum =  120
'''