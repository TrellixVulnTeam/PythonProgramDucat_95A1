from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.title("Malware Scanner")
root.geometry("700x500")
root.configure(background='#FFFFFF')
t = Frame(root, width = 600, height = 60, bd=1, bg='yellow', relief=SUNKEN)
b = Frame(root, width = 100, height = 200, bd=1, bg='skyblue', relief=SUNKEN)
labelWidget = Frame(root, width = 200, height = 250, bd=1, bg='blue', relief=SUNKEN)
label2Widget = Frame(root, width = 600, height = 90, bd=1, bg='green', relief=SUNKEN)
t.grid(row = 0, column = 0)
labelWidget.grid(row = 1, column = 0)
label2Widget.grid(row = 2, column = 0)
b.grid(row = 1, column = 1)
a=Label(t,text="Label : ")
a.grid(row=2,column=10)
a=Label(b,text="Label : ")
root.mainloop()