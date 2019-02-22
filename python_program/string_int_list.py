# string , int , float , complex print in list , int print in list ....???

a=[1,2,3,4,5,"hello","python","color","nehru",4,5,8,9,10,10.25,.36,5.89,12.154,5j,6j,78j,12+45j]
b=[]
c=[]
d=[]
e=[]
z=[]
for x in a:
	if type(x)==str:
		print("string== ",x)
		b.append(x)
		
	elif type(x)==float:
		print("float== ",x)
		c.append(x)
	elif type(x)==complex:
		print("complex== ",x)
		d.append(x)
	else:
		print("int== ",x)
		e.append(x)
print("string type list : == ",b)
print("float type list : == ",c)
print("complex type list : == ",d)
print("int type list : == ",e)
z=b+c+d+e
print("total print all list 'string' + 'float' + 'complex' + 'int' type list ====  ",z)