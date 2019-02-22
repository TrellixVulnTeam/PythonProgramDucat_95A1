#########  application of GUI interpriture  using python tkinter ..??   *****************


#from tkinter import *
#import tkinter

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms

win = tk.Tk()
win.title(" GUI APPLICATION ")

# create label , button , radiobutton , checkbox ....
# widgets --   create label , button , radiobutton , checkbox , tk , ttk  .... etc.
# label use mostly two type pack and grid (why default the label is create in middle but use gird and set row or column.)
# label use  =====   pack , grid

# 1.  create label 


id_label = ttk.Label(win,text="ENTER THE ID : ")
id_label.grid(row=1,column=0,sticky=tk.W)

name_label = ttk.Label(win,text="ENTER THE NAME : ")
name_label.grid(row=2,column=0,sticky=tk.W)

email_label = ttk.Label(win,text="ENTER THE EMAIL : ")
email_label.grid(row=3,column=0,sticky=tk.W)

age_label = ttk.Label(win,text="ENTER THE AGE : ")
age_label.grid(row=4,column=0,sticky=tk.W)

address_label = ttk.Label(win,text="ENTER THE ADDRESS : ")
address_label.grid(row=5,column=0,sticky=tk.W)

Parents_name_label = ttk.Label(win,text="ENTER THE FATHER'S NAME : ")
Parents_name_label.grid(row=6,column=0,sticky=tk.W)

gender_label = ttk.Label(win,text="SELECT THE GENDER  : ")
gender_label.grid(row=7,column=0,sticky=tk.W)


# 2. create entry box .


id_var = tk.IntVar()
id_entrybox = ttk.Entry(win , width=20 , text=id_var)
id_entrybox.grid(row=1,column=2)
id_entrybox.focus()

name_var = tk.StringVar()
name_entrybox = ttk.Entry(win , width=20 , textvariable = name_var)
name_entrybox.grid(row=2,column=2)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win , width=20 , textvariable = email_var)
email_entrybox.grid(row=3,column=2)

age_var = tk.IntVar()
age_entrybox = ttk.Entry(win , width=20 , text=age_var)
age_entrybox.grid(row=4,column=2)

address_var = tk.StringVar()
address_entrybox = ttk.Entry(win , width=20 , textvariable = address_var)
address_entrybox.grid(row=5,column=2)

Parents_name_var = tk.StringVar()
Parents_name_entrybox = ttk.Entry(win , width=20 , textvariable = Parents_name_var)
Parents_name_entrybox.grid(row=6,column=2)



# 3. create dropdown/combobox  button .

gender_var = ttk.Combobox(win , width=17 , values=("select gender","male","female","other") , state='readonly')
gender_var.set("select gender")
gender_var.grid(row=7,column=2)


# 4. create Radio button .

usertype = tk.StringVar()
radio_btn1 = ttk.Radiobutton(win, text="Student" , value="student" , variable= usertype)
radio_btn1.grid(row=8, column=0)

radio_btn2 = ttk.Radiobutton(win, text="Teacher" , value="Teacher" , variable= usertype)
radio_btn2.grid(row=8, column=1)

radio_btn3 = ttk.Radiobutton(win, text="Docter" , value="Docter" , variable= usertype)
radio_btn3.grid(row=8, column=2)

# 5. create check button .

checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win,text="check if you want to subscribe to our newslatter .", variable= checkbtn_var)
checkbtn.grid(row=9,columnspan=4) 


# 6. create submit button .


def action():

    userid = id_var.get()
    username = name_var.get()
    userage = age_var.get()
    usermail = email_var.get()
    useraddress = address_var.get()
    userparentsname = Parents_name_var.get()
    usergender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get()==0:
        subscribed = "No"
    else:
        subscribed = "Yes" 
    print(f'ID OF USER : ===  {userid}\nNAME OF USER : ===  {username}S\O Mr {userparentsname}\n')
    print(f'AGE USER : ===  {userage}\nGMAIL OF USER : ===  {usermail}\nGENDER OF USER : ====  {usergender}\n')
    print(f'PASSION OF USER : ===  {user_type}\nSubscribed : ===  {subscribed}\n')
    print(f'ADDRESS OF USER : ===  {useraddress}\n')
    print(f'massage successfully imported in the application of GUI interpeter of python code ....\n')
    print("************************************    End entry of user  *****************************************")
    ms.showinfo("Success Entry ")

    #print(f'My id {userid}\nusername {username}\n S/O {userparentsname}\nAm{userage} years old \nmy mail is {usermail} \nDestination is {useraddress}\n ')
    
submit_button = tk.Button(win, text = "Submit" , command = action)
submit_button.grid(row=10,column=0)


win.mainloop()
