# first project_6/2/2019.. use by tinkter ...??


from pymysql import *
from tkinter import *
from tkinter import messagebox as tm
from MyAdmin import *
from MyUser import *
class MyLogin(Frame):
	def __init__(self,master):
		super().__init__(master)
		
		self.l1=Label(self,text='User Name',fg='blue')
		self.t1=Entry(self)
		self.l2=Label(self,text='Password', fg='blue')
		self.t2=Entry(self,show='*')
		self.b1=Button(self,text='login',fg='blue',command=self.check)
		
		self.l1.grid(row=0,column=0)
		self.t1.grid(row=0,column=1)
		
		self.l2.grid(row=1,column=0)
		self.t2.grid(row=1,column=1)
		
		self.b1.grid(columnspan=2)
		self.pack()
		
	def check(self):
		con=connect(db='ducat',user='root',passwd='root',host='localhost')
		cur=con.cursor()
		username=self.t1.get()
		password=self.t2.get()
		self.t1.delete(0,'end')
		self.t2.delete(0,'end')
		result=cur.execute("select * from login where userid='%s' and passwd='%s'"%(username,password))
		record=cur.fetchone()
		if result==1:
			utype=record[2]
			if utype=='admin':
				#tm.showinfo('Correct','Admin Section')
				root1=Tk()
				ob1=AdminForm(root1)
				root1.title('Admin')
				root1.geometry('100x150')
				root1.mainloop()
			else:
				root2=Tk()
				ob1=UserForm(root2)
				root2.title('User Form')
				root2.geometry('300x150')
				root2.mainloop()
		else:
			tm.showinfo('Error','either username or password is incorrect')
root=Tk()
obj=MyLogin(root)
root.title('Login Form')
root.geometry('200x110')
root.mainloop()
