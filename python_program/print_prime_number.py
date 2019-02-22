# Python Print Prime Numbers  ???

n = int(input("enter the range print prime no ===>>>> :"))
for i in range(2,n+1):
	for j in range(2,i):
		if i%j == 0:
			break
	else:
		print("prime number : ")
		print(i)

		
'''
output ==

enter the range print prime no ===>>>> :50
prime number :
2
prime number :
3
prime number :
5
prime number :
7
prime number :
11
prime number :
13
prime number :
17
prime number :
19
prime number :
23
prime number :
29
prime number :
31
prime number :
37
prime number :
41
prime number :
43
prime number :
47

'''