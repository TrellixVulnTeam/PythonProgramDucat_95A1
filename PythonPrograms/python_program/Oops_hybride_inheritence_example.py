# Hybride inheritence example using by Oops class ...??

class Student():
	def get_details(self):
		self.name = input("enter the student name : ")
		self.rollno = int(input("enter the student roll no : "))
		self.age = int(input("enter the student age : "))

class Subject(Student):
	def get_subject(self):
		self.p = int(input("enter the physics marks : "))
		self.c = int(input("enter the chemistry marks : "))
		self.m = int(input("enter the math marks : "))
		self.h = int(input("enter the hindi marks : "))
		self.e = int(input("enter the english marks : "))
		
		
class Sports(Student):
	def get_sports(self):
		self.phy = int(input("enter the physical sports marks : "))
		
		
class Result(Subject,Sports):
	def get_calculate(self):
		self.total = self.p + self.c + self.m + self.h + self.e + self.phy
		self.avg = self.total / 6
		if (self.avg >=90):
			self.grade = "A+"
		elif (self.avg >=80):
			self.grade = "A"
		elif (self.avg >=70):
			self.grade = "B+"
		elif (self.avg >=60):
			self.grade = "B"
		elif (self.avg >=50):
			self.grade = "C"
		elif (self.avg >=40):
			self.grade = "D"
		elif (self.avg >=33):
			self.grade = "E"
		elif (self.avg >=0):
			self.grade = "F"
			
		else:
			self.grade = "SORRY."

	def display(self):
	
		print("------------------------   MARKSHEAT OF THE STUDENT -----------------------------")
		print("Student Name              : ",self.name)
		print("Student Roll number       : ",self.rollno)
		print("Student age               : ",self.age)
		print("                                                                                 ")
		print("------------------------      STUDENT RESULT   -----------------------------")
		print("Physics marks     		 : ",self.p)
		print("Chemistry marks   	     : ",self.c)
		print("Math marks                : ",self.m)
		print("Hindi marks               : ",self.h)
		print("English marks             : ",self.e)
		print("                                                                                 ")
		print("---------------------------------  SPORTS MARKS  -----------------------------------------")
		print("Sports marks              : ",self.phy)
		print("Total marks out of 600    :    =================================================")
		print("Agrigate marks of 600     : ",self.total)
		print("                                                                                 ")
		print("Student Result is total percentage of marksheet with grade and numbers : =====")
		print("                                                                                 ")
		print("Percentage                : ",round(self.avg,2) ,"%")
		print("Grade                     : ",self.grade ,"grade")

		
s = Result()
s.get_details()
s.get_subject()
s.get_sports()
s.get_calculate()		
s.display()




'''
output ===


# first result  =====>>>>>>>>>>>>>>>>>

enter the student name : SAURABH SHUKLA
enter the student roll no : 7896850
enter the student age : 21
enter the physics marks : 78
enter the chemistry marks : 89
enter the math marks : 96
enter the hindi marks : 78
enter the english marks : 58
enter the physical sports marks : 86
------------------------   MARKSHEAT OF THE STUDENT -----------------------------
Student Name              :  SAURABH SHUKLA
Student Roll number       :  7896850
Student age               :  21

------------------------      STUDENT RESULT   -----------------------------
Physics marks                    :  78
Chemistry marks              :  89
Math marks                :  96
Hindi marks               :  78
English marks             :  58

---------------------------------  SPORTS MARKS  -----------------------------------------
Sports marks              :  86
Total marks out of 600    :    =================================================
Agrigate marks of 600     :  485

Student Result is total percentage of marksheet with grade and numbers : =====

Percentage                :  80.83 %
Grade                     :  A grade



# second result  =====>>>>>>>>>>>>>>>>>

enter the student name : Saurabh mishra
enter the student roll no : 45796
enter the student age : 21
enter the physics marks : 78
enter the chemistry marks : 92
enter the math marks : 89
enter the hindi marks : 54
enter the english marks : 65
enter the physical sports marks : 89
------------------------   MARKSHEAT OF THE STUDENT -----------------------------
Student Name              :  saurabh
Student Roll number       :  45796
Student age               :  21

------------------------      STUDENT RESULT   -----------------------------
Physics marks                    :  78
Chemistry marks              :  92
Math marks                :  89
Hindi marks               :  54
English marks             :  65

---------------------------------  SPORTS MARKS  -----------------------------------------
Sports marks              :  89
Total marks out of 600    :    =================================================
Agrigate marks of 600     :  467

Student Result is total percentage of marksheet with grade and numbers : =====

Percentage                :  77.83 %
Grade                     :  B+ grade


'''
