from ast import Return
from tkinter import*
import time
import random
from tkinter import messagebox

def Questions():    
    number1 = random.randrange(1,9)
    number2 = random.randrange(11,50)
    answer = number1 + number2
    prompt = ("ADD " + str(number1) + " and " + str(number2))
    label1 = Label(root, text=prompt, width=len(prompt), bg='yellow')
    label1.pack()
    return answer

def start(event):
    global count_flag 
    global answer
    answer = Questions()
    count_flag = True
    count = 0.0
    while True:
        if count_flag == False:
            break
        # put the count value into the label
        label['text'] = str(count)
        # wait for 0.1 seconds
        time.sleep(0.1)
        # needed with time.sleep()
        root.update()
        # increase count
        count += 0.1
    entryWidget.delete(0,"end")#Automatically clears input when next one is entered

# def Submit(answer, entryWidget, event):
#      """ Display the Entry text value. """
#      global count_flag

#      count_flag = False
#      print(answer)

#      if entryWidget.get().strip() == "":
#          messagebox.showerror("Tkinter Entry Widget", "Please enter a number.")

#      if answer != int(entryWidget.get().strip()):
#          messagebox.showinfo("Answer", "INCORRECT!")
#      else:
#          messagebox.showinfo("Answer", "CORRECT!")


def Submit(answer, entryWidget):
     """ Display the Entry text value. """
     global count_flag

     count_flag = False
     print(answer)

     if entryWidget.get().strip() == "":
         messagebox.showerror("Tkinter Entry Widget", "Please enter a number.")

     if answer != int(entryWidget.get().strip()):
         messagebox.showinfo("Answer", "INCORRECT!")
     else:
         messagebox.showinfo("Answer", "CORRECT!")
     entryWidget.delete(0,"end")

     





# create a Tkinter window
root = Tk()

root.title("Math Quiz")
root["padx"] = 40
root["pady"] = 20   
root.configure(background='blanched almond')

# Create a text frame to hold the text Label and the Entry widget
textFrame = Frame(root,bg="blanched almond")
#directions     
directions = ('Click start to begin. You will be asked a series of questions.')
instructions = Label(root, text=directions, width=len(directions),height=2,bg='blanched almond',font=('Helvetica 15 bold italic'))
instructions.pack(pady=20)

btn_start = Button(root, text="Start(s)",width=10,height=1,font=('Helvetica 10 bold italic'))
btn_start.pack(pady=20)
root.bind('<s>', start)
btn_start.bind('<Button-1>',start) #for Left Click


#Create a Label in textFrame
entryLabel = Label(textFrame,borderwidth=10,width=10,font=('Helvetica 10 bold italic'))
entryLabel["text"] = "Answer:"
entryLabel.pack(side=LEFT)

# def validate(value_if_allowed,
#                        prior_value, text, validation_type, trigger_type, widget_name):
#         if value_if_allowed:
#             try:
#                 float(value_if_allowed)
#                 return True
#             except ValueError:
#                 return False
#         else:
#             return False

# vcmd = ((validate),
#                 '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
# text1 = Entry(textFrame,borderwidth=5,width=20, validate = 'key', validatecommand = vcmd)
# # text1.grid()
# text1.focus()
def only_numbers(char):
    return char.isdigit()


validation = textFrame.register(only_numbers)
entryWidget = Entry(textFrame,borderwidth=5,width=20, validate="key", validatecommand=(validation, '%S'))
entryWidget.pack(side=LEFT,padx=10)
# w = Entry(textFrame, validate='all', validatecommand=(vcmd, '%P')) 
# w.pack(side=LEFT,padx=10)



# Create an Entry Widget in textFrame
# entryWidget = Entry(textFrame,borderwidth=5,width=20)
# entryWidget["width"] = 25
# entryWidget["height"] = 2
# text1.pack(side=LEFT,padx=10)

textFrame.pack()


# this will be a global flag
count_flag = True


Sub = lambda: Submit(answer, entryWidget)
#stopwatch = lambda: start(answer)

# create needed widgets
label = Label(root, text='0.0',font=('Helvetica 10 bold italic'))
btn_submit = Button(root, text="Submit(Enter)",width=10,height=1,command=Sub,font=('Helvetica 10 bold italic'))
# btn_submit.bind('<Enter>',Sub)
# btn_start.bind('<Enter>',start)
btn_submit.pack(pady=10)
label.pack(pady=10)
root.bind('<Return>',lambda event: Submit(answer, entryWidget))
#Clearing Entry Box
# def clear():
#     entryWidget.delete(0,END)

# btn = Button(root, text="Clear(c)",font=('Helvetica 10 bold italic'))
# root.bind('<c>',lambda event: clear)
# btn.pack()
# start the event loop
label11 = Label(root,text="""Note:
                             1.Press 's' to start   
                             2.Press 'Enter' to 
                             Submit
                             3.Press 'c' to Clear
""",font=('Helvetica 8 bold italic'),bg="blanched almond")
label11.place(relx=0.78,rely=0.84)
# label11.pack(side=LEFT)
root.mainloop()
