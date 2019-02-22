from tkinter import *
root=Tk()
lb1=Label(text="This is My Label 1")
lb2=Label(text="This is My Label 2",bg="Sky Blue")
lb3=Label(text="This is My Label 3",bg="Green",fg="Red")
lb1.pack()
lb2.pack(side=LEFT)
lb3.pack(side=RIGHT)
root.mainloop()