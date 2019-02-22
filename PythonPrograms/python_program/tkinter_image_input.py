from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root =Tk(className='|--Garibon ka Image Enhanced--|')
root.geometry('450x500')
def open_command():
	a = filedialog.askopenfile(parent=root,title='select a file')
	if a !=None:
		print(a)
		img = PhotoImage(file=a.name)
		label = Label(image=img)
		label.pack()

def exit_command():
    if messagebox.askyesno('Do you want to Exit',
                              'if you quit you will come on road'):
        root.destroy()

def about_command():
    label = messagebox.showinfo('About','This Editor is created by Himanshu')

def ref():
    root.geometry('225x250')
    print('your window size smallied')

def b2n():
    root.geometry('450x500')
    print('your window is normalised')

menu = Menu(root)
root.config(menu = menu)

filemenu = Menu(menu)
menu.add_cascade(label='File',menu=filemenu)

filemenu.add_command(label='New')
filemenu.add_command(label='open',command=open_command)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=exit_command)
filemenu.add_separator()
filemenu3 = Menu(menu)
menu.add_cascade(label='Option',menu=filemenu3)
filemenu3.add_command(label='Resize window',command = ref)
filemenu3.add_command(label='Back to Normal',command = b2n)
filemenu3.add_separator()


helpmenu = Menu(menu)
menu.add_cascade(label='help',menu=helpmenu)
helpmenu.add_command(label='About...',command=about_command)

root.mainloop()
