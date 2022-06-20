from tkinter import *
from word2number import w2n
from num2words import num2words

top = Tk()
top.geometry("700x700")
L1 = Label(top, text="User Name")
L1.pack()


def only_numbers(char):
    return char.isdigit()

# def clear():
#     entryWidget.delete(0,"end")

def clear(event):
    entryWidget.delete(0,"end")
    text1.delete("1.0","end")
    
def getValue(event):
	value = entryWidget.get()
    # Label(top, text=value+"=", font= ('Century 15 bold')).pack(pady=20);Label(top, text=num2words(value), font= ('Century 15 bold')).pack(pady=20)
	print(num2words(value));text1.insert(END,num2words(value))

# def getValue1():
# 	value = entryWidget.get()
# 	print(num2words(value))


validation = top.register(only_numbers)
entryWidget = Entry(top,borderwidth=5,width=30, validate="key", validatecommand=(validation, '%S'),font=('Helvetica 12 bold italic'))
entryWidget.pack()

text1 = Text(top,border=5,relief=RAISED,yscrollcommand=True,wrap=WORD,width=52,height=8,font=('Helvetica 15 bold italic'))
text1.pack(padx=10,pady=10)

button= Button(top, text="Submit(Enter)", command= getValue,font=('Helvetica 15 bold italic'))
button.pack()
top.bind('<Return>',getValue)
button.bind('<Button-1>',getValue)

button1 = Button(top,text="Clear(c)",command=clear,font=('Helvetica 15 bold italic'))
button1.pack()
top.bind('<c>',clear)
button1.bind('<Button-1>',clear)

top.mainloop()