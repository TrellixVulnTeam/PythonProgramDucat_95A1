from tkinter import *
root=Tk()
b1=Button(text="This My Button One")
b2=Button(text="This My Button Two",bg="SkyBlue")
b3=Button(text="This My Button Three",bg="Yellow",fg="Red")
b1.pack(side=TOP)
b2.pack(side=LEFT)
b3.pack(side=RIGHT)
root.mainloop()