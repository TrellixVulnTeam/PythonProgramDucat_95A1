# output == {"name":['ram','shyam'],"class":[5,6],"age":[10,11]}

n= int(input("range:" ))
a={}
for x in range(1,n+1):
	k = input("key : ")
	b = []
	m = int(input("users choice of value : ")) 
	for i in range(1,m+1):
		v = input("values : ")
		b.append(v)
	a[k] = b
print(a)

# searing values : in index values:===>>>

# print(a['key'][list index value.])   ===????


'''
output ===

range:3
key : ram
users choice of value : 3
values : salary
values : 20000
values : HCL
key : shyam
users choice of value : 3
values : salary
values : 25000
values : TCS
key : sita
users choice of value : 3
values : salary
values : 30000
values : WIPRO
{'ram': ['salary', '20000', 'HCL'], 'shyam': ['salary', '25000', 'TCS'], 'sita': ['salary', '30000', 'WIPRO']}

'''