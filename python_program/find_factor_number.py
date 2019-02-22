#  Python Find Factors of Number  ???

n = int(input("enter the no find factor : "))
print("total no hers factors : ")
for i in range(1,n+1):
	if n%i == 0:
		print(i)
		
'''
output ==

enter the no find factor : 50
1
2
5
10
25
50

'''