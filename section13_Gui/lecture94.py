# การจัดการ Layout ของ widget
from tkinter import *

def sayHello() :
    print("Hello World!!")

mainWindow = Tk()
button1 = Button(mainWindow,text="Click me 1",command=sayHello).grid(row=0,column=1)
button2 = Button(mainWindow,text="Click me 2",command=sayHello).grid(row=0,column=2)
button3 = Button(mainWindow,text="Click me 3",command=sayHello).grid(row=1,column=1)

mainWindow.mainloop()
