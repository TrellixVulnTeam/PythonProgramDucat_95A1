# databases of the create student profile in add student data ..??
# data as likes  id , name , address , mob ..??

from pymysql import *
class Student:
	def __init__(self):
		self.con = connect(db = 'ducat_jan_py' , user = 'root' ,password = 'saurabh' ,host = 'localhost')
		self.cur = self.con.cursor()
		
	def addstudent(self):
		id = int(input("Enter the Id: "))
		name = input("Enter the Name: ")
		age = int(input("Enter the student Age: "))
		address = input("Enter the Address: ")
		mob = int(input("Enter the Contect number: "))
		self.cur.execute("Insert into student values(%d,'%s',%d,'%s',%d)"%(id,name,age,address,mob))
		self.con.commit()
	
	def showdetails(self):
		self.cur.execute("select * from student")
		self.cur.execute("select * from student")
		result = self.cur.fetchall()
	    #print(result)
		print("===============================================")
		print("id\tname\tage\taddress\tmob")
		print("===============================================")
		for x in result:
			print("%d\t'%s'\t%d\t'%s'\t%d"%(x[0],x[1],x[2],x[3],x[4]))
		print("===============================================")
		
	def finddetail(self):
		id = int(input("Enter the Id: "))
		self.cur.execute("select * from student where id='%s'"%(id))
		result = self.cur.fetchall()
		#print(result)
		print("===============================================")
		print("id\tname\tage\taddress\tmob")
		print("===============================================")
		for x in result:
			print("%d\t'%s'\t%d\t'%s'\t%d"%(x[0],x[1],x[2],x[3],x[4]))
		print("===============================================")
		
	def deletestudent(self):
		id = int(input("Enter the Id : "))
		self.cur.execute("delete from student where id=%d"%id)
		self.con.commit()
		print("Record Deleted succesfully.")
		
	def updatestudent(self):
		id = int(input("Enter the Id: "))
		name = input("Enter the Name: ")
		age = int(input("Enter the student Age: "))
		address = input("Enter the Address: ")
		mob = int(input("Enter the Contect number: "))
		self.cur.execute("update student set name='%s',age=%d,address='%s',mob=%d where id=%d"%(name,age,address,mob,id))
		self.con.commit()
		
a = Student()
while True:
	print("press 1 to add \n press 2 to show \n press 3 to find \n press 4 to delete \n press 5 to update \n press 6 to exit")
	
	c = int(input("Enter the user choice : "))
	
	if (c == 1):
		a.addstudent()
		
	elif (c == 2):
		a.showdetails()
		
	elif (c == 3):
		a.finddetail()
		
	elif (c == 4):
		a.deletestudent()
		
	elif (c == 5):
		a.updatestudent()
		
	elif (c == 6):
		break
		#exit()
		
	else:
		print("wrong input by user.")
		
a.con.close()






		
		


'''


                    %%%%%%%%%%%%%%%%%%%    first step of the database run programm ....????    %%%%%%%%%%%%%%%%

# create data in databases first then run the server again in python quary ...??    ***************##

# $  mysql -u root -p
# Enter password: *******    # saurabh



$  mysql> create database ducat_jan_py;


$  mysql> show databases;


$   mysql> use google;
o/t == Database changed

$  mysql> show tables;

$  mysql> select * from client;

                                     %%%%%%%%%%%%%%%%%%%    second step of the database run programm ....????    %%%%%%%%%%%%%%%%

									 
									 
$ Desktop>mysql -u root -p
Enter password: *******

$ mysql> use ducat_jan_py;
o/t == Database changed

$ mysql>  create table student(id int(5) primary key , name varchar(50),age int ,address varchar(50),mob int);



            %%%%%%%%%%%%%%%%%%%    third step of the database run programm ....????    %%%%%%%%%%%%%%%% 

			
output ===

press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 1
Enter the Id: 111
Enter the Name: saur
Enter the student Age: 45
Enter the Address: intupara
Enter the Contect number: 986859656
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 1
Enter the Id: 456
Enter the Name: vinit
Enter the student Age: 28
Enter the Address: kanpur
Enter the Contect number: 789658654
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 1
Enter the Id: 125
Enter the Name: sharda
Enter the student Age: 49
Enter the Address: kanpur
Enter the Contect number: 789658549
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 1
Enter the Id: 450
Enter the Name: sapna
Enter the student Age: 22
Enter the Address: kalayanpur
Enter the Contect number: 789658456
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 1
Enter the Id: 451
Enter the Name: saurabh
Enter the student Age: 23
Enter the Address: IIT kanpur
Enter the Contect number: 789685487
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 1
Enter the Id: 454
Enter the Name: rishabh
Enter the student Age: 26
Enter the Address: kanoj
Enter the Contect number: 789658496
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 455
wrong input by user.
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 1
Enter the Id: 455
Enter the Name: swati
Enter the student Age: 25
Enter the Address: petempura
Enter the Contect number: 785964896
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 2
===============================================
id      name    age     address mob
===============================================
111     'saur'  45      'intupara'      986859656
125     'sharda'        49      'kanpur'        789658549
450     'sapna' 22      'kalayanpur'    789658456
451     'saurabh'       23      'IIT kanpur'    789685487
452     'saurabh'       21      'noida' 789685986
454     'rishabh'       26      'kanoj' 789658496
455     'swati' 25      'petempura'     785964896
456     'vinit' 28      'kanpur'        789658654
===============================================
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 3
Enter the Id: 455
===============================================
id      name    age     address mob
===============================================
455     'swati' 25      'petempura'     785964896
===============================================
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 4
Enter the Id : 455
Record Deleted succesfully.
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 2
===============================================
id      name    age     address mob
===============================================
111     'saur'  45      'intupara'      986859656
125     'sharda'        49      'kanpur'        789658549
450     'sapna' 22      'kalayanpur'    789658456
451     'saurabh'       23      'IIT kanpur'    789685487
452     'saurabh'       21      'noida' 789685986
454     'rishabh'       26      'kanoj' 789658496
456     'vinit' 28      'kanpur'        789658654
===============================================
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 5
Enter the Id: 452
Enter the Name: swati
Enter the student Age: 25
Enter the Address: kanoj
Enter the Contect number: 789685965
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 2
===============================================
id      name    age     address mob
===============================================
111     'saur'  45      'intupara'      986859656
125     'sharda'        49      'kanpur'        789658549
450     'sapna' 22      'kalayanpur'    789658456
451     'saurabh'       23      'IIT kanpur'    789685487
452     'swati' 25      'kanoj' 789685965
454     'rishabh'       26      'kanoj' 789658496
456     'vinit' 28      'kanpur'        789658654
===============================================
press 1 to add
 press 2 to show
 press 3 to find
 press 4 to delete
 press 5 to update
 press 6 to exit
Enter the user choice : 6

                         %%%%%%%%%%%%%%%%    end program  %%%%%%%%%%%%%%%%%%


'''





	
		
		
		
		
	