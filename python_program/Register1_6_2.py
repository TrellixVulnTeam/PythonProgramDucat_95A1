from pymysql import *
from tkinter import *
from tkinter import messagebox as mb
class RegisterForm(Frame):
	def __init__(self,master):
		super().__init__(master)
		self.l1=Label(self,text='User Name',fg='blue')
		self.l2=Label(self,text='Password', fg='blue')
		self.l3=Label(self,text='First Name',fg='blue')
		self.l4=Label(self,text='Last Name',fg='blue')
		self.l5=Label(self,text='Father Name',fg='blue')
		self.l6=Label(self,text='Qualification',fg='blue')
		self.l7=Label(self,text='Address',fg='blue')
		self.l8=Label(self,text='City',fg='blue')
		self.l9=Label(self,text='Mobile No',fg='blue')
		self.l10=Label(self,text='User Type',fg='blue')
		
		self.t1=Entry(self)
		self.t2=Entry(self,show="*")
		self.t3=Entry(self)
		self.t4=Entry(self)
		self.t5=Entry(self)
		self.t6=Entry(self)
		self.t7=Entry(self)
		self.t8=Entry(self)
		self.t9=Entry(self)
		self.t10=Entry(self)
		
		self.b1=Button(self,text='Save',command=self.save)
		self.l1.grid(row=0,column=0)
		self.t1.grid(row=0,column=1)
		
		self.l2.grid(row=0,column=2)
		self.t2.grid(row=0,column=3)
		
		self.l3.grid(row=1,column=0)
		self.t3.grid(row=1,column=1)
		
		self.l4.grid(row=1,column=2)
		self.t4.grid(row=1,column=3)
		
		self.l5.grid(row=2,column=0)
		self.t5.grid(row=2,column=1)
		
		self.l6.grid(row=2,column=2)
		self.t6.grid(row=2,column=3)
		
		self.l7.grid(row=3,column=0)
		self.t7.grid(row=3,column=1)
		
		self.l8.grid(row=3,column=2)
		self.t8.grid(row=3,column=3)
		
		self.l9.grid(row=4,column=0)
		self.t9.grid(row=4,column=1)
		
		self.l10.grid(row=4,column=2)
		self.t10.grid(row=4,column=3)
		
		self.b1.grid(columnspan=4)
	
		self.pack()
	def save(self):
		con=connect(db='ducat',user='root',passwd='root',host='localhost')
		cur=con.cursor()
		uid=self.t1.get()
		pwd=self.t2.get()
		fname=self.t3.get()
		lname=self.t4.get()
		father=self.t5.get()
		quali=self.t6.get()
		addr=self.t7.get()
		city=self.t8.get()
		mobile=self.t9.get()
		utype=self.t10.get()
		cur.execute("insert into login values('%s','%s','%s')"%(uid,pwd,utype))
		con.commit()
		cur.close()
		cur1=con.cursor()
		cur1.execute("insert into register values('%s','%s','%s','%s','%s','%s','%s','%s')"%(uid,fname,lname,father,quali,addr,city,mobile))
		con.commit()
		cur1.close()
		self.t1.delete(0,'end')
		self.t2.delete(0,'end')
		self.t3.delete(0,'end')
		self.t4.delete(0,'end')
		self.t5.delete(0,'end')
		self.t6.delete(0,'end')
		self.t7.delete(0,'end')
		self.t8.delete(0,'end')
		self.t9.delete(0,'end')
		self.t10.delete(0,'end')
		con.close()
		mb.showinfo('Confirmation','Record Save')
	
		

Register.py

Open with






