from tkinter import *
root=Tk()
lb=Label(text="Login Form")
lb.grid(row=0,column=1)

l=Label(text="Mail")
l2=Label(text="Password")

txt1=Entry()
txt2=Entry()

l.grid(row=1,column=0,stick="S")
txt1.grid(row=1,column=1)

l2.grid(row=2,column=0)
txt2.grid(row=2,column=1,stick="W")

check=Checkbutton(text="Remember Password")
check.grid(columnspan=2)
root.mainloop()
