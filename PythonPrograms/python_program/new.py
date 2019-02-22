from tkinter import *
from tkinter import messagebox as ms
from pymysql import *
root=Tk()
root.geometry('500x500')
root.title("Registration Form")
def add():
	con=connect(db="root",user="root",password="root",host="localhost")
	cur=con.cursor()
	cur.execute("insert into user values('%s','%s','%s','%s',%d)"%
	(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),int(entry_5.get())))
	con.commit()
	print("Record Inserted")
	con.close()
	entry_1.delete(0,'end')
	entry_2.delete(0,'end')
	entry_3.delete(0,'end')
	entry_4.delete(0,'end')
	entry_5.delete(0,'end')
	
	ms.showinfo("Submit","Registered")
def login():
	global entry_21,entry_22
	root1=Tk()
	root1.geometry('250x250')
	label_21=Label(root1,text="User Name",font=("bold",10))
	label_21.place(x=38,y=45)
	entry_21=Entry(root1)
	entry_21.place(x=68,y=75)
	label_22=Label(root1,text="Password",font=("bold",10))
	label_22.place(x=38,y=105)
	entry_22=Entry(root1,show='*')
	entry_22.place(x=68,y=135)
	Button(root1,text='Log In',width=20,bg='brown',fg='white',command=search).place(x=90,y=190)
	root1.mainloop()
def search():
	con=connect(db="root",user="root",password="root",host="localhost")
	cur=con.cursor()
	cur.execute("Select uname,password from user where uname = '%s'"%(entry_21.get()))
	result=cur.fetchone()
	print(result)
	#print(type(entry_22.get()))
	if(result[1]==int(entry_22.get()) and result[0]==entry_21.get()):
		ms.showinfo("Login","loged in succesfully")
	else:	
		ms.showinfo("Login","loged in unsuccesfull")
	con.commit()
	con.close()
label_0=Label(root,text="Registration Form",width=20,font=("bold",20))
label_0.place(x=90,y=53)
label_1=Label(root,text="First Name",width=20,font=("bold",10))
label_1.place(x=80,y=130)
entry_1=Entry(root)
entry_1.place(x=240,y=130)

label_2=Label(root,text="Last Name",width=20,font=("bold",10))
label_2.place(x=68,y=180)
entry_2=Entry(root)
entry_2.place(x=240,y=180)

label_3=Label(root,text="User Name",width=20,font=("bold",10))
label_3.place(x=68,y=230)
entry_3=Entry(root)
entry_3.place(x=240,y=230)

label_4=Label(root,text="Email",width=20,font=("bold",10))
label_4.place(x=68,y=280)
entry_4=Entry(root)
entry_4.place(x=240,y=280)

label_5=Label(root,text="Password",width=20,font=("bold",10))
label_5.place(x=68,y=330)

entry_5=Entry(root,show='*')
entry_5.place(x=240,y=330)


Button(root,text='Submit',width=20,bg='red',fg='white',command=add).place(x=270,y=380)
Button(root,text='Log In',width=20,bg='red',fg='white',command=login).place(x=90,y=380)

root.mainloop()
