# Python Program to Print all Prime Numbers in an Interval   ????

n= int(input("enter the number of range b/w find the prime number : "))
for i in range(2,n+1):
	for j in range(2,i):
		if i%j==0:
			break
	else:
		print(i)
		
'''
output == 
range  17
prime numbers ==
2
3
5
7
11
13
17
'''