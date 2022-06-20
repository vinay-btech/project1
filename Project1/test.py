from tkinter import *
import random

root =Tk()
root.geometry('700x700')
root.configure(background='cyan')




capital_dic={
    'Andhra Pradesh': 'Montgomery',
    'Arunachal Pradesh': 'Itanagar',
    'Assam':'Dispur',
    'Bihar':'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa':'Panaji',
    'Gujarat':'Gandhinagar',
    'Haryana':'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizwal',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata',
      
} # create a dictionary, key is the state and value is the capital
States=list(capital_dic.keys())
label1 =Label(root,text='Let\'s learn Indian States and Capitals. 10 rounds..',font=('Helvetica 15 bold italic'))
label1.pack()
point=0 # this is the score
def question():
    for i in range(10):
        state=random.choice(States) # randomly select 10 states, how do I avoid duplicate?
        capital = capital_dic[state]
        # user_guess = input('what is the capital of %s?'%state )
        # text2 = Text(root,text='what is the capital of ',font=('Helvetica 15 bold italic'))
        # text2.pack(padx=20,pady=20)
        # entry1 = Entry(root)
        # entry1.insert(0,state)
        # entry1.pack(padx=20,pady=20)
        text1 = Text(root,border=5,relief=RAISED,yscrollcommand=True,wrap=WORD,width=52,height=8,font=('Helvetica 15 bold italic'),background='dark slate gray',foreground="White")
        text1.pack(padx=10,pady=10)
        text1.insert(END,state)

        if user_guess.lower() == 'exit':  #if a user type in exit, the game exits
            break
        elif user_guess.title() == capital:
            point+=1
            print('Correct! Your score is %d' %point)
        else:
            print('Incorrect. The capital of {} is {}.'.format(state,capital))
    print('We are done. Your final score is %d, thank you.' %point)

button1 = Button(root,text="Clear(c)",command=question,font=('Helvetica 15 bold italic'))
button1.pack()

root.mainloop()