from tkinter import *
from change import *
class UserForm(Frame):
	def __init__(self,abc):
		super().__init__(abc)
		
		self.b1=Button(self,text='Sale',command=self.sale)
		self.b2=Button(self,text='Change Password',command=self.change)
		self.b3=Button(self,text='Exit',command=self.quit)
		
		
		self.b1.grid(row=0,column=0)
		self.b2.grid(row=0,column=1)
		self.b3.grid(row=0,column=2)
		
		self.pack()
		
	def quit(self):
		exit(0)
	def sale(self):
		pass
	def change(self):
		root=Tk()
		obj=ChangePasswd(root)
		root.title('Password Change')
		root.geometry('250x300')
		root.mainloop()
