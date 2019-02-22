# data employee nameId.text file write to write program....????

import sys
print("1. exiting user.")
print("2. new user.")
ch = int(input("choice : "))
if ch == 1:
	exit()
elif ch == 2:
	while(1):
		name = input("enter the employee name : ")
		company_name = input("enter the company_name : ")
		empId= int(input("enter the id of employee : "))
		address = input("enter the address of employee : ")
		basic_salary = float(input("enter the salary : "))
		hra = basic_salary / 2
		da = basic_salary / 10
		ta = basic_salary / 10
		fund = basic_salary * 12 / 100
		cut_salary =( basic_salary * num_leaves )/25
		gross_salary =( basic_salary + hra + da + ta - fund - cut_salary )
		age = int(input("enter the age : "))
		num_leaves = int(input("enter the num_leaves : "))
		f = open("C:/Users/Saurabh/Desktop/file_handle/employee_data/"+name+str(empId)+".txt","a")
		f.write(name+'\n')
		f.write(company_name+'\n')
		f.write(str(empId)+'\n')
		f.write(address+'\n')
		f.write(str(gross_salary)+'\n')
		f.write(str(age)+'\n')
		f.write(str(num_leaves)+'\n')
		f.close()
		choice = input("Do you want to continue y/n : ")
		if choice == 'n':
			f = open("C:/Users/Saurabh/Desktop/file_handle/employee_data/"+name+str(empId)+".txt","r")
			print(f.read())
			choice1 = input("Do you want to search any data ( name + empId ) y/n : ")
			if choice1 == 'y':
				name = input("enter the employee name : ")	
				empId= int(input("enter the id of employee : "))
				f = open("C:/Users/Saurabh/Desktop/file_handle/employee_data/"+name+str(empId)+".txt","r")
				print(f.read())
			else:
				exit()
			sys.exit(1)
else:
	print("thankyou for watching in company.")
		





'''

output ===


enter the employee name : ram
enter the company_name : hcl
enter the id of employee : 4000
enter the address of employee : dehli
enter the salary : 56986.36
enter the age : 24
enter the num_leaves : 2
Do you want to continue y/n : y
enter the employee name : ram bhadur
enter the company_name : tcs
enter the id of employee : 7800
enter the address of employee : kalayanpur
enter the salary : 45897.36
enter the age : 21
enter the num_leaves : 2


Do you want to continue y/n : n
ram bhadur
tcs
7800
kalayanpur
45897.36
21
2



Do you want to search any data ( name + empId ) y/n : y
enter the employee name : ram
enter the id of employee : 4000
ram
hcl
4000
dehli
56986.36
24
2

enter the employee name : roshni
enter the company_name : wipro
enter the id of employee : 4500
enter the address of employee : kanpur
enter the salary : 45968
enter the age : 25
enter the num_leaves : 2
Do you want to continue y/n : y
enter the employee name : sita kumari
enter the company_name : tsc
enter the id of employee : 7800
enter the address of employee : palampur
enter the salary : 45006
enter the age : 42
enter the num_leaves : 3
Do you want to continue y/n : n
sita kumari
tsc
7800
palampur
71109.48000000001
42
3

Do you want to search any data ( name + empId ) y/n : y
enter the employee name : ram
enter the id of employee : 4000
ram
hcl
4000
dehli
56986.36
24
2


'''		