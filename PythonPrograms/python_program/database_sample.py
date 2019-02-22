from pymysql import *
class DataBase:
	def __init__(self):
		self.con = connect(db="batch600",user="root",password="root",
					 host="localhost")
		self.cur = self.con.cursor()
	
	def add(self):
		id = int(input("Enter Id : "))
		name = input("Enter Name  : ")
		age = int(input("Enter Age : "))
		try:	
			self.cur.execute("insert into register values(%d,'%s',%d)"
					%(id,name,age))
			self.con.commit()
			print("Data inserted")
		except:
			print("Error Occured")
			self.con.close()
	
	def show(self):
		self.cur.execute("select * from Register")
		data = self.cur.fetchall()
		print("======================")
		print("ID\tName\tAGE")
		print("======================")
		for x in data:
			print("%s\t%s\t%s"%(x[0],x[1],x[2]))
		print("======================")	
	
	def update(self):
		id = int(input("Enter Id To Update : "))
		name = input("Enter Your Name : ")
		try:	
			self.cur.execute("update register set name = '%s' where id = '%d'"%(name,id))
			self.con.commit()
			print("Updated")
		except:
			print("id not found")