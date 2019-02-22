from tkinter import *      
root = Tk()      
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack()      
img=PhotoImage(file="Resturant.png")      
canvas.create_image(50,20, anchor=NW, image=img)      
root.mainloop()