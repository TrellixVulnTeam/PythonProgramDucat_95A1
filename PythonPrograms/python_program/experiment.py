from tkinter import *
import smtplib
import time
from tkinter import scrolledtext

ser=smtplib.SMTP('smtp.gmail.com',587)
ser.starttls()
def index():
	ser.login(e1.get(),e2.get())
	message=e4.get('1.0',END +'-1c')
	f=e3.get('1.0',END +'-1c')
	f=f.split()
	print("===========")
	print(message)
	for x in f:
		ser.sendmail(e1.get(),x,message)
		print(time.ctime())
	print("Done DANA DAN")
r=Tk()
r.geometry("700x500")
r.title("REGISTRATION FORM")
l=Label(r,text="Mail FORM",font=("bold",40),fg="Green")
l.pack()

s=Label(r,text="Sender Gmail id : >",font=("bold",20),fg="Green")
s.place(x=0,y=50)

e1=Entry(r)
e1.place(x=350,y=60,width=300,height=20)

s1=Label(r,text="Sender Gmail PassWord : >",font=("bold",20),fg="Green")
s1.place(x=0,y=100)

e2=Entry(r)
e2.place(x=350,y=108,width=300,height=20)

s2=Label(r,text="Recivers EMAIL ID : >",font=("bold",20),fg="Green")
s2.place(x=0,y=150)

e3 = scrolledtext.ScrolledText(r, width=100, height=80)
e3.place(x=350,y=150,width=300,height=60)

s3=Label(r,text="Message : >",font=("bold",20),fg="Green")
s3.place(x=0,y=240)

e4 = scrolledtext.ScrolledText(r, width=100, height=80)
e4.place(x=350,y=250,width=300,height=80)

b1=Button(r,text="SUBMIT",width=40,bg="Red",command=index)
b1.place(x=300,y=400)
r.mainloop()