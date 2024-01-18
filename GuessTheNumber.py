from tkinter.ttk import*
from tkinter import*


window = Tk()
window.title('Welcome')
window.geometry('800x800')
upArrow=PhotoImage(file="uparrow.png")
downArrow=PhotoImage(file="downarrow.png")
correct=PhotoImage(file="correct.png")
dice=PhotoImage(file="die.png")
def Exit():
    window.destroy()

rb = StringVar()
rb.set("Easy")
tries = 0
number = 0
def check(event):
    global number
    global upArrow
    global downArrow
    global correct
    global diceLbl
    global var
    global tries
    global triesLbl
    global txt

    if int(txt.get()) == number:
        diceLbl.configure(image=correct)
        tries = tries + 1
        lbl4.configure(text="Tries: " + str(tries))
        btn2.configure(state=ACTIVE)
        tries = 0
    elif int(txt.get()) > number:
        diceLbl.configure(image=downArrow)
        tries = tries + 1
        lbl4.configure(text="Tries: " + str(tries))
        btn2.configure(state=ACTIVE)
    elif int(txt.get()) < number:
        diceLbl.configure(image=upArrow)
        tries = tries + 1
        lbl4.configure(text="Tries: " + str(tries))
        btn2.configure(state=ACTIVE)

    txt.delete(0, 'end')

def Randomise():
    global number
    global hard
    hard = rb.get()
    import random
    tries = 0
    lbl4.configure(text="Tries: " + str(tries))
    diceLbl.configure(image=dice)
    if hard == 'Easy':
        number = random.randint(0,50)
    if hard == 'Normal':
        number = random.randint(0,100)
    if hard == 'Hard':
        number = random.randint(0,200)










lbl = Label(window, text = 'Guess The Number',font=('Helvetica', 40, 'bold'))
lbl.place(x=170, y=5)


rad1 = Radiobutton(window, text = 'Easy(0-50)', value = 'Easy',variable = rb)
rad1.place(x=100, y=100)

rad2 = Radiobutton(window, text = 'Normal(0-100)', value = 'Normal',variable = rb)
rad2.place(x=300, y=100)

rad3 = Radiobutton(window, text = 'Hard(0-200', value = 'Hard',variable = rb)
rad3.place(x=500, y=100)


lbl2 = Label(window, text = 'In this game you will try to find a secret number. ',font=('Helvetica', 15, 'bold'))
lbl2.place(x=150, y=200)

lbl3 = Label(window, text = 'You must do it with the least possible tries!', font=('Helvetica', 15, 'bold'))
lbl3.place(x=170, y=230)

btn = Button(window, text = 'EXIT',font=('Helvetica', 15, 'bold'), command=Exit)
btn.place(x=730, y=400)

btn2 = Button(window, text='RANDOMISE',font=('Helvetica', 15, 'bold'), command=Randomise)
btn2.place(x=650, y=450)

txt = Entry(window, width=20)
txt.place(x=320, y=400)

lbl4 = Label(window, text='Tries:', font=('Helvetica', 15, 'bold'))
lbl4.place(x=330, y=350)


diceLbl = Label(window, image=dice, font=('Helvetica', 15, 'bold'))
diceLbl.place(x=50, y=400)
window.bind('<Return>',check)


















































































window.mainloop()
