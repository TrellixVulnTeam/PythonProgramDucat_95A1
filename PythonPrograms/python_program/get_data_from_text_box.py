from tkinter import *
from tkinter import messagebox as ms
root=Tk()
root.geometry("500x500")
def display():
	s=txt.get()
	print(s)
	ms.showinfo("Message","Hello "+s)
l=Label(text="Enter Your Name : ")
txt=Entry()
b1=Button(text="This My Button One",command=display)
l.place(x=25,y=50)
txt.place(x=50,y=100)
b1.place(x=100,y=200)
root.mainloop()