import tkinter as tk

source = tk.Tk()

def iQuiz(source,row=0,column=0,rowspan=None,columnspan=None):
    storeObj=tk.Frame(source,bg="powder blue")
    storeObj.grid(row=row,column=column,rowspan=rowspan,columnspan=columnspan)
    return storeObj

def button(source,text,command=None,row=0,column=0,rowspan=None,columnspan=None):
    storeObj=tk.Button(source,text=text,command=command)
    storeObj.grid(row=row,column=column,rowspan=rowspan,columnspan=columnspan)
    return storeObj

def radioButton(source,text,indicator='off',command=None,row=0,column=0,rowspan=None,columnspan=None):
    storeObj=tk.Radiobutton(source,text=text,indicator=indicator,command=command)
    storeObj.grid(row=row,column=column,rowspan=rowspan,columnspan=columnspan)
    return storeObj

def label(source,text,row=0,column=0,rowspan=None,columnspan=None):
    storeObj=tk.Label(source,text=text)
    storeObj.grid(row=row,column=column,rowspan=rowspan,columnspan=columnspan)
    return storeObj





class Application(tk.Frame):

    def __init__(self,title):
        tk.Frame.__init__(self)
        self.master.title(title)
        self.option_add('*Font','aerial 20 bold')
        self.pack(expand=tk.YES, fill=tk.BOTH)

        #widget for quiz app
        frame=iQuiz(self,column=1)
        frame.config(width=1000,height=500)
        frame.grid_propagate(0)
        que_label=label(frame,"question is here",row=1)
        opt1=radioButton(frame,"Option A is here",row=2)
        opt2=radioButton(frame,"Option B is here",row=3)
        opt3=radioButton(frame,"Option C is here",row=4)
        opt4=radioButton(frame,"Option D is here",row=5)
        ans_label=label(frame,"\nanswer will be shown on click of show me answer",row=6)
        answer=button(frame,"Show me answer",row=7)


        frame_pre=iQuiz(self,column=0)
        pre=button(frame_pre,'Previous')
        pre.config(bg='Powder blue',fg='white')

        frame_next=iQuiz(self,column=2)
        nxt=button(frame_next,'Next')
        nxt.config(bg='powder blue',fg='white')



if __name__=='__main__':
    Application('Quiz App').mainloop()







