from tkinter import *
from ttk import*


root = Tk()
root.title("Study GUI")
root.geometry("1000x570")

num_var = StringVar()
word_var = StringVar()





#Frames
frame1 = Frame(root,width=1000,height=570,bg="cyan").pack()
frame2 = Frame(frame1,width=500,height=500, bg="light green").place(relx=.5,rely=.5,anchor=CENTER)


Button1 = Button(frame2,text="Maths")
Button1.pack()


#name_label = Label(frame2,text="Enter a Number in numerical:", font=('Calibre',10,'bold'))
#name_entry = Entry(frame2,textvariable = num_var, font=('calibre',10,'normal'))
#
#passw_label = Label(frame2, text = 'Enter a Number in Words', font = ('calibre',10,'bold'))
#passw_entry=Entry(frame2, textvariable = word_var, font = ('calibre',10,'normal'))
#
#sub_btn=Button(frame2,text = 'Submit', command = submit)
#
#name_label.grid(row=0,column=0)
#name_entry.grid(row=0,column=1)
#passw_label.grid(row=1,column=0)
#passw_entry.grid(row=1,column=1)
#sub_btn.grid(row=2,column=1)


#menu


root.mainloop()

