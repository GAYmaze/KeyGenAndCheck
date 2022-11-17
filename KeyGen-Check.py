import tkinter as tk
from tkinter import *
import random
Characters = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!'

def createkey():
    password = ''
    for c in range(20):
        password+= random.choice(Characters)

    with open ('KeysTutorial.txt', mode='a') as myfile:
        myfile.write(str(password)+'\n')
        myfile.close()

    print(password)

def false():
    print('Key Is Not Valid.')

def length():
    key = Textbox.get(1.0, tk.END+"-1c")
    if len(key) > 20:
        false()
        return
    elif len(key) <= 19:
        false()
        return
    else:
        checkkey()

def checkkey():
    key = Textbox.get(1.0, tk.END+"-1c")
    with open ('KeysTutorial.txt') as f:
        if (key) in f.read():
            print('Key is Valid')
            return
        else:
            false()

mainframe = Tk()
mainframe.title('Tutorial')
mainframe.resizable(0,0)
mainframe.geometry('500x300')
mainframe.configure(bg= 'Black')
button = Button(mainframe, text = 'Make key', padx = 30, command=createkey, bg = 'White')
button.place(x=1, y=1)
button1 = Button(mainframe, text = 'Check key', padx = 30, command=length, bg = 'White')
button1.place(x=1, y=50)
Textbox = Text(mainframe, height=1, width =20)
Textbox.pack(pady= 1, padx=50)
mainframe.mainloop()

#Use at your own will
