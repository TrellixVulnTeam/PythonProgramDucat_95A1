# data of employee company sturcture ...????

import sys
list1 = []
def new():

	while True:
		id = int(input("enter the id : "))
		name = input("enter the name : ")
		age = int(input("enter the age : "))
		add = input("enter the address : ")
		salary = int(input("enter the salary : "))
		leaves = int(input("enter the leaves : "))
		da = salary * (0.1)
		ta = salary * (0.05)
		hra = salary * (0.08)
		fund = salary * (0.1)
		l = (salary * leaves )/ 30
		g_salary = salary + hra + da + ta -fund -l
		g_s = round(g_salary,2)
		f = open("C:/Users/Saurabh/Desktop/file_handle/emp_data/"+name+str(id)+".txt","a")
		
		f.write((str(id)+','+name+','+str(age)+','+add+','+str(g_s))+','+str(leaves))
		f.write('\n')
		f.seek(0)
		f.close()
		list1.append([id,name,age,add,g_s,leaves])
		flag = input("To be continue y/n : ")
		if flag == 'n':
			z = input("do you want to update any record y/n : ")
			if z == 'y':
				update()
			sys.exit()
			
	
		
def main_screen():
	print("1. exiting user.")
	print("2. new user.")
	ch = int(input("enter the choice of user : "))
	return ch
	
def main():
	print("1. search data . ")
	print("2. read data . ")
	c = int(input("enter the user choice search read or update data choice : "))
	return c
	
def search():
	name = input("enter the employee name : ")
	f=open("C:/Users/Saurabh/Desktop/file_handle/emp_data/"+name+".txt","r")
	print(f.read())
		
def read():
	f = open("C:/Users/Saurabh/Desktop/file_handle/emp_data/"+name+str(id)+".txt","r")
	a = f.read()
	print(a)
	f.close()
	
def update():
	name = input("enter the employee name : ")
	id = int(input("enter the id number of employee :"))
	print("1. add ")
	print("2. age ")
	print("3. salary ")
	print("4. leaves ")
	choice1 = int(input("enter the update value : "))
	print(list1)
	for i in list1:
		if i[0] == id and i[1] == name:
			if choice1 == 1:
				add1 = input("enter the address update : ")
				i[3]=add1
			elif choice1 == 2:
				age1 = int(input("enter the age update : "))
				i[2]=age1
			elif choice1 == 3:
				salary = int(input("enter the basic salary update value : "))
				da = salary * (0.1)
				ta = salary * (0.05)
				hra = salary * (0.08)
				fund = salary * (0.1)
				l = (salary * leaves )/ 30
				g_salary = salary + hra + da + ta -fund -l
				g_s = round(g_salary,2)
				i[4]=g_s
			elif choice1 == 4:
				leaves1 = int(input("enter the leaves : "))
				i[5]=leaves1
		
		f = open("C:/Users/Saurabh/Desktop/file_handle/emp_data/"+name+str(id)+".txt","w")
		f.write(str(i[0])+','+i[1]+','+str(i[2])+','+i[3]+','+str(i[4])+','+str(i[5]))
		f.write('\n')		
		f.close()
print(list1)	
while True:
	choice = main_screen()
	if choice == 2:
		new()
	elif choice == 1:
		c = main()
		if c == 1:
			search()
		elif c == 2:
			read()
		else:
			exit()
	else:
		sys.exit()
	
	



'''

output ===

1. exiting user.
2. new user.
enter the choice of user : 2
enter the id : 400
enter the name : ram
enter the age : 23
enter the address : kanpur
enter the salary : 25000
enter the leaves : 2
To be continue y/n : y
enter the id : 450
enter the name : shyam
enter the age : 45
enter the address : noida
enter the salary : 50000
enter the leaves : 4
To be continue y/n : n



'''	