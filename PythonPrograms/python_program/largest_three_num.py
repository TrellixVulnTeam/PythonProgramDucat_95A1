# Python Program to Find the Largest Among Three Numbers  ????

a= int(input("enter the first no. "))
b= int(input("enter the second no. "))
c= int(input("enter the third no. "))

if (a>b and a>c):
	print("first no is largest",a)
elif (b>c and b>a):
	print("second no is largest",b)
else:
	print("third no is largest",c)
	

'''
a=87
b=76
c=108
output ===  third no is largest.
'''



# find the lagest no , minimin no in user input ...???

a=[]
n= int(input("enter the range "))
for i in range(1,n+1):
	m= int(input("enter the no is append in list."))
	a.append(m)
print(a)
print("maximum number of total list range given by user input :: == ",max(a))
print("minimum number of total list range given by user input :: == ",min(a))

'''
range=5
45
54
56
21
12
output == 
max number is list == 56
min number is list == 12
'''
	