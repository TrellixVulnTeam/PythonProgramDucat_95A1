# list all value append name,industry name,address,salary ...??  append and delete user choice etc ....??

a=[]
n=int(input("enter the range "))
for i in range(1,n+1):
	b=[]
	name=input("enter the employe name : ")
	industry_name=input("enter the industry name : ")
	address=input("enter the address name : ")
	salary=float(input("enter the salary of employe : "))

	b.append(name)
	b.append(industry_name)
	b.append(address)
	b.append(salary)
	a.append(b)
print(a)
print("choice 1 is name : ")
print("choice 2 is industry_name : ")
print("choice 3 is address : ")
print("choice 4 is salary : ")
print("choice 5 if user want to del : ")
print("choice 6 if user want to add data : ")

choice= int(input("enter the choice by users : "))

if choice == 1:
	name = input("enter the name of employe :")
	for i in range(len(a)):
		if name == a[i][0]:
			print(a[i])
elif choice == 2:
	name = input("enter the name of employe :")
	for i in range(len(a)):
		if name == a[i][1]:
			print(a[i])
elif choice == 3:
	name = input("enter the name of employe :")
	for i in range(len(a)):
		if name == a[i][2]:
			print(a[i])
elif choice == 4:
	name = input("enter the name of employe :")
	for i in range(len(a)):
		if name == a[i][3]:
			print(a[i])
			
			
elif choice == 5:
	n = int(input('Enter choice for deletion 1. name, 2. industry_name, 3. address, 4.salary'))
	if n == 1:
		name = input("enter the name of employe :")
		for i in range(len(a)):
			if name == a[i][0]:
				del a[i]
				print(a)
				break
	elif n == 2:
		name = input("enter the name of employe :")
		for i in range(len(a)):
			if name == a[i][1]:
				del a[i]
				print(a)
				break
	elif n == 3:
		name = input("enter the name of employe :")
		for i in range(len(a)):
			if name == a[i][2]:
				del a[i]
				print(a)
				break
	elif n == 4:
		name = input("enter the name of employe :")
		for i in range(len(a)):
			if name == a[i][3]:
				del a[i]
				print(a)
				break
	else:
		print("invalid choice of user want to delete data ")


elif choice ==6:
	b=[]
	name=input("enter the employe name : ")
	industry_name=input("enter the industry name : ")
	address=input("enter the address name : ")
	salary=float(input("enter the salary of employe"))

	b.append(name)
	b.append(industry_name)
	b.append(address)
	b.append(salary)
	a.append(b)
	print(a)
else:
	print("invalid choice. ")




'''
output ==  

enter the range 3
enter the employe name : 11
enter the industry name : 21
enter the address name : 31
enter the salary of employe41
enter the employe name : 111
enter the industry name : 211
enter the address name : 311
enter the salary of employe411
enter the employe name : 1111
enter the industry name : 3111
enter the address name : 4111
enter the salary of employe3222
[['11', '21', '31', 41.0], ['111', '211', '311', 411.0], ['1111', '3111', '4111', 3222.0]]
choice 1 is name :
choice 2 is industry_name :
choice 3 is address :
choice 4 is salary :
enter the choice by users : 2
enter the name of employe :21
['11', '21', '31', 41.0]

'''