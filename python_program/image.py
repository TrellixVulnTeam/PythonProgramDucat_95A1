from tkinter import *
root=Tk()
img = PhotoImage("pattern.png")
panel = Label(root,image=img)
panel.place(x=45,y=65)
root.mainloop()		