# My_admin.py   program in tinkter ...??


from tkinter import *
from Register import *
class AdminForm(Frame):
	def __init__(self,abc):
		super().__init__(abc)
		
		self.b1=Button(self,text='Register',command=self.register)
		self.b2=Button(self,text='Purchage',command=self.purchage)
		self.b3=Button(self,text='Delete',command=self.delete)
		self.b4=Button(self,text='Update',command=self.updt)
		
		self.b1.grid(row=0,column=1)
		self.b2.grid(row=1,column=1)
		self.b3.grid(row=2,column=1)
		self.b4.grid(row=4,column=1)
		
		self.pack()
		
	def register(self):
		root=Tk()
		obj=RegisterForm(root)
		root.title('Registration Form')
		root.geometry('450x200')
		root.mainloop()
	def purchage(self):
		pass
	def delete(self):
		pass
	def updt(self):
		pass