# remove 1 in a list (given also) .....???

######  1.

a= [1,1,2,1,3,1,5,1,6,1,1,1,6,1,7,1,8,1,9]
b=[]
# c=0
for i in range(len(a)):
	if (a[i]!=1):
		b.append(a[i])
'''                         # find how many time coming the 1 value in list then using counter part ..
	else:
		c=c+1
print(c)
'''
print(b)



#######  2.

a= [1,1,2,1,3,1,5,1,6,1,1,1,6,1,7,1,8,1,9]
b=[]
for x in a:
	if x==1:
		pass
	else:
		b.append(x)
print(b)



#######  3.

a= [1,1,2,1,3,1,5,1,6,1,1,1,6,1,7,1,8,1,9]
b=[]
for x in a:
	if x==1:
		continue
	else:
		b.append(x)
print(b)



#######  4.

a= [1,1,2,1,3,1,5,1,6,1,1,1,6,1,7,1,8,1,9]
b=[]
for x in a:
	if x!=1:
		b.append(x)
print(b)


#######  5.

a=[1,1,1,1,8,9,1,5,1,1,1,10,11]
b=[]
for x in a:
	if x==1:
		continue
'''
	print(x)           # beacuse continue statement the value can skip any 1 in list so another value in b to append in list value of the condition level ...
'''
	b.append(x)
print(b)
	
	
#######  6.

a= [1,1,2,1,3,1,5,1,6,1,1,1,6,1,7,1,8,1,9]
for x in a:
	if x==1:
		a.remove(x)
print(a)


'''  # because the value of index in one time iterate then next time after next itterate value index because the value can update next list a[0] iterate after next time a[1]   ...
o/t ===   [2, 3, 5, 6, 6, 7, 1, 8, 1, 9]
'''


