from tkinter import *
from tkinter import messagebox as ms
from pymysql import *
root=Tk()#sudo apt-get install tk8.5
#sudo apt-get install tk8.5
def add():
	con=connect(db="name",user="root",password="root",host="localhost")
	cur=con.cursor()
	cur.execute("insert into data values('%s','%s')"%(txt1.get(),txt2.get()))
	con.commit()
	print("Record Inserted")
	con.close()
	ms.showinfo("Submit","Registered")
def show():
        con=connect(db="name",user="root",password="root",host="localhost")
        cur=con.cursor()
        cur.execute("select * from data")
        root1=Tk()
        result=cur.fetchall()
        y=1
        for x in result:
                a=Label(root1,text=result)
                a.grid(row=y,column=1)
                y+=1
first=Label(root,text="First Name : ")
last=Label(root,text="Last Name : ")
b1=Button(text="Register Here",command=add)
b2=Button(text="Show Here",command=show)
txt1=Entry()
txt2=Entry()

first.grid(row=0,column=0)
txt1.grid(row=0,column=1)

last.grid(row=1,column=0)
txt2.grid(row=1,column=1)
b1.grid(row=2,column=1)
b2.grid(row=2,column=0)
root.mainloop()
