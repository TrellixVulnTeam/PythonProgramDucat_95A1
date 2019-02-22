from tkinter import *
import smtplib
import time
ser=smtplib.SMTP('smtp.gmail.com',587)
ser.starttls()
def index():
	ser.login(e1.get(),e2.get())
	message=e4.get()
	f=e3.get()
	f=f.split(',')
	print(f)
	for x in f:
		ser.sendmail(e1.get(),x,message)
		print(time.ctime())
	print("Done DANA DAN")
r=Tk()
r.geometry("1080x800")
r.title("REGISTRATION FORM")
l=Label(r,text="Mail FORM",font=("bold",40),fg="Green")
l.pack()

s=Label(r,text="Sender Gmail id : ",font=("bold",20),fg="Green")
s.place(x=100,y=200)

e1=Entry(r)
e1.place(x=400,y=200,width=600,height=40)

s1=Label(r,text="Sender Gmail PassWord : ",font=("bold",20),fg="Green")
s1.place(x=100,y=300)

e2=Entry(r)
e2.place(x=400,y=300,width=600,height=40)

s2=Label(r,text="Recivers EMAIL ID",font=("bold",20),fg="Green")
s2.place(x=100,y=400)

e3=Entry(r)
e3.place(x=400,y=400,width=600,height=40)

s3=Label(r,text="Message",font=("bold",20),fg="Green")
s3.place(x=100,y=500)

e4=Entry(r)
e4.place(x=400,y=500,width=400,height=80)
b1=Button(r,text="submitted",width=40,bg="Red",command=index)
b1.place(x=600,y=600)
r.mainloop()