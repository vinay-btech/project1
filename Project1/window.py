#From PIP install pyinputplus
#from pip install turtle
from re import I
from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Study GUI")
        master.geometry("1000x870")
        master.config(bg="light cyan")  

        # self.label = Label(master, text="This is our first GUI!")
        # self.label.pack()

        mylabel1 = Label(root,background="light grey", text="Please Select the Subject From Below list:",font=('Helvetica 25 bold italic'))
        mylabel1.pack()
        mylabel1.place(in_=root,anchor='c',relx=.50,rely=.08)

        myFrame2 = Frame(root, width=500,height=500,background='light green')
        myFrame2.place(in_=root,anchor="c",relx=.5,rely=.5)
        
        self.myButton1 = Button(myFrame2,text="Maths(Cal)",width=10, height=1,command=self.Maths, font=('Helvetica 20 bold italic'),borderwidth=10)
        self.myButton1.place(in_=myFrame2,relx=0.05,rely=0.1)
        # # self.myButton1.pack(pady=10)

        self.myButton4 = Button(myFrame2,text="English",width=10, height=1,command=self.English,font=('Helvetica 20 bold italic'),borderwidth=10)
        # self.myButton1.pack(pady=10)
        # # self.myButton1.grid(row=1,column=1)
        self.myButton4.place(in_=myFrame2,relx=0.05,rely=0.3)

        self.myButton2 = Button(myFrame2,text="num/words",width=10, height=1,command=self.Maths1,font=('Helvetica 20 bold italic'),borderwidth=10)
        # # self.myButton1.pack(pady=10)
        # self.myButton1.grid(row=0,column=1)
        self.myButton2.place(in_=myFrame2,relx=0.56,rely=0.1)

        self.myButton3 = Button(myFrame2,text="Social",width=10, height=1,command=self.Social,font=('Helvetica 20 bold italic'),borderwidth=10)
        # self.myButton1.pack(pady=10)
        # # self.myButton1.grid(row=1,column=0)
        self.myButton3.place(in_=myFrame2,relx=0.56,rely=0.3)

        self.myButton5 = Button(myFrame2,text="Game1",width=10, height=1,command=self.Game1,font=('Helvetica 20 bold italic'),borderwidth=10)
        # self.myButton1.pack(pady=10)
        # # self.myButton1.grid(row=1,column=1)
        self.myButton5.place(in_=myFrame2,relx=0.05,rely=0.5)

        self.myButton6 = Button(myFrame2,text="Game2",width=10, height=1,command=self.Game2,font=('Helvetica 20 bold italic'),borderwidth=10)
        # self.myButton1.pack(pady=10)
        # # self.myButton1.grid(row=1,column=1)
        self.myButton6.place(in_=myFrame2,relx=0.56,rely=0.5)
        
        self.myButton8= Button(myFrame2,text="Exit",width=8, height=1,command=self.Exit,font=('Helvetica 8 bold italic'),borderwidth=5)
        # self.myButton1.pack(pady=10)
        # # self.myButton1.grid(row=1,column=1)
        self.myButton8.place(in_=myFrame2,relx=0.45,rely=0.9)
        

        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack()

        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

    # def greet(self):
    #     print("Greetings!")
    def Maths(self):
        import Maths
    def English(self):
        print("English Button Clicked")

    def Maths1(self):
        import Maths1

    def Social(self):
        print("Social Button Clicked")
    def Game1(self):
        import game1

    def Game2(self):
        import game2

    def Exit(self):
        root.quit()


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()