# database 3 python code ..??


import sqlite3
class DBHelper():
	def __init__(self):
		self.conn=sqlite3.connect("sample.db")
		self.c=self.conn.cursor()
		self.c.execute("CREATE TABLE IF NOT EXISTS `student`(`id`	INTEGER,`name` TEXT,`age` INTEGER,`gender` TEXT,PRIMARY KEY(`id`));")
		self.c.execute("CREATE TABLE IF NOT EXISTS 'att'(student_id INTEGER,att Text,FOREIGN KEY (student_id) references student(id));")
	def add(self):
		self.c.execute("insert into att values(%d,'%s')"%(101,'A'))
		self.conn.commit()
	def show(self):
		self.c.execute("select * from att")
		data = self.c.fetchall()
		print(data)
a=DBHelper()
a.add()
a.show()