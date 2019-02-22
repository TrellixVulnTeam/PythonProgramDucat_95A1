from tkinter import *
from pymysql import *
class PurchageForm(Frame):
	def __init__(self,master):
		super().__init__(master)
		
		self.l1=Label(self,text='Product Id')
		self.l2=Label(self,text='Product Name')
		self.l3=Label(self,text='Description')
		self.l4=Label(self,text='Unit Price')
		self.l5=Label(self,text='Quantity')
		self.l6=Label(self,text='Date of Purchase')
		
		self.t1=Entry(self)
		self.t2=Entry(self)
		self.t3=Entry(self)
		self.t4=Entry(self)
		self.t5=Entry(self)
		self.t6=Entry(self)
		
		self.b1=Button(self,text='Save')
		
		self.l1.grid(row=0,column=0)
		self.t1.grid(row=0,column=1)
		
		self.l1.grid(row=1,column=0)
		self.t1.grid(row=1,column=1)
		
		self.l2.grid(row=2,column=0)
		self.t2.grid(row=2,column=1)
		
		self.l3.grid(row=3,column=0)
		self.t3.grid(row=3,column=1)
		
		self.l4.grid(row=4,column=0)
		self.t4.grid(row=4,column=1)
		
		self.l5.grid(row=5,column=0)
		self.t5.grid(row=5,column=1)
		
		self.l6.grid(row=6,column=0)
		self.t6.grid(row=6,column=1)
		
		self.b1.grid(columnspan=2)
		self.pack()
		

purchase.py

Open with






