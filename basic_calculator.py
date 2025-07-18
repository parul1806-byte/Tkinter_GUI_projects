#import tkinter
from idlelib.configdialog import font_sample_text
from tkinter import *
#GUI interaction
window = Tk()
window.geometry("400x400")
window.title("CALCULATOR")


#input
#1 creating a entery box
e = Entry(width=60,borderwidth=5)
e.pack()

def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))

button1 = Button(window,text='1', width=13, command=lambda :click(1))
button1.place(x=17,y=60)

button2 = Button(window,text='2', width=13, command=lambda :click(2))
button2.place(x=150,y=60)

button3 = Button(window,text='3', width=13, command=lambda :click(3))
button3.place(x=280,y=60)


button4 = Button(window,text='4', width=13, command=lambda :click(4))
button4.place(x=17,y=110)

button5 = Button(window,text='5', width=13, command=lambda :click(5))
button5.place(x=150,y=110)

button6 = Button(window,text='6', width=13, command=lambda :click(6))
button6.place(x=280,y=110)

button7 = Button(window,text='7', width=13, command=lambda :click(7))
button7.place(x=17,y=160)

button8 = Button(window,text='8', width=13, command=lambda :click(8))
button8.place(x=150,y=160)

button9 = Button(window,text='9', width=13, command=lambda :click(9))
button9.place(x=280,y=160)

button10 = Button(window,text='0', width=13, command=lambda :click(0))
button10.place(x=17,y=210)

def add():
    n1 = e.get()
    global i
    global math
    math = "addition"
    i = int(n1)
    e.delete(0,END)
button11 = Button(window,text='+', width=13, command=add)
button11.place(x=150,y=210)
def sub():
    n1 = e.get()
    global i
    global math
    math = "subtraction"
    i = int(n1)
    e.delete(0,END)
button12 = Button(window,text='-', width=13, command=sub)
button12.place(x=280,y=210)
def mul():
    n1 = e.get()
    global i
    global math
    math = "multiplication"
    i = int(n1)
    e.delete(0,END)
button12 = Button(window,text='*', width=13, command=mul)
button12.place(x=17,y=260)
def div():
    n1 = e.get()
    global i
    global math
    math = "division"
    i = int(n1)
    e.delete(0,END)
button12 = Button(window,text='/', width=13, command=div)
button12.place(x=150,y=260)
def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,i + int(n2))
    elif math == "subtraction":
        e.insert(0,i - int(n2))
    elif math == 'multiplication':
        e.insert(0,i * int(n2))
    elif math == "division":
        e.insert(0,i / int(n2))

button12 = Button(window,text='=', width=13,command=equal )
button12.place(x=280,y=260)
def clear():
    e.delete(0,END)
button13 = Button(window,text='clear', width=13,command=clear )
button13.place(x=17,y=310)







#mainloop
window.mainloop()