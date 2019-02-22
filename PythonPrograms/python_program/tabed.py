import tkinter as tk                   
from tkinter import ttk
win = tk.Tk()                           
win.title("Python GUI")              
win.geometry('500x500')
tabControl = ttk.Notebook(win) 
tab1 = ttk.Frame(tabControl)    
tabControl.add(tab1, text='Add Employee')
tabControl.pack(expand=1, fill="both")
tab2 = ttk.Frame(tabControl)    
tabControl.add(tab2, text='Department')
tabControl.pack(expand=1, fill="both")

la=tk.Label(tab1,text="Registration Form",font=("bold",20))
la1=tk.Label(tab2,text="Form",font=("bold",20))
la.place(x=100,y=200)
la1.place(x=100,y=400)
win.mainloop()          