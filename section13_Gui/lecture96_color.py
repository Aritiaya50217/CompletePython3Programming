from tkinter import *

def sayHello() :
    print("Hello World!!")

mainWindow = Tk()

button1 = Button(mainWindow,text="Click me 1",command=sayHello,width=20).grid(row=0,column=1)
button2 = Button(mainWindow,text="Click me 2",command=sayHello).grid(row=0,column=2)
button3 = Button(mainWindow,text="Click me 3",command=sayHello).grid(row=1,column=1)
# กำหนด size ของ widget ด้วย width คือ ความกว้าง height คือ ความสูง
# Foreground การใส่สีตัวอักษร
# background สีพื้นหลัง
label = Label(text="Hello World",width=20,fg="white",bg="lightgray").grid(row=0,column=0) 
mainWindow.mainloop()
