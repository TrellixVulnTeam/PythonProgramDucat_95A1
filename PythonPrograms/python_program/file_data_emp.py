# append file to file data ...????

f = open("C:\\Users\\Saurabh\\Desktop\\file_handle\\file_data_emp.cpp","a")
for i in range(5):
	a = input("enter the name : ")
	b = int(input("enter the age : "))
	c = int(input("enter the class : "))
	f.write("name : "+a+'\n')
	f.write("age : "+str(b)+'\n')
	f.write("class : "+str(c)+'\n')
print("file created.")
f.close()


'''
output  ====

file created.
another file data ...???

name : ramu
age : 45
class : 5
name : shyam
age : 78
class : 12
name : sita
age : 45
class : 26
name : raju
age : 40
class : 12
name : roshni
age : 40
class : 15



'''