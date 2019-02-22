# Python Program to Find Factors of Number  ????
                         # or  **************
# python program to find the divisable 

n= int(input("enter the number : "))
print("total divisable : ")
i=1
while n >= i:
	if n%i == 0:
		print(i)
	i=i+1
	
			
'''
n= 45
output == 
1
3
5
9
15
45
'''