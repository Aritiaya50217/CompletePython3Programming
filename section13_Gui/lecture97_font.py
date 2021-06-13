from tkinter import *

mainWindow = Tk()
# font = ("ชื่อ font ที่ต้องการใช้",ขนาดตัวอักษร)
# anchor = ใส่ตำแหน่งที่ต้องการ (W = ซ้าย ,E = ขวา)
text1 = Label(mainWindow,text="Hello World",width=20,fg="black",bg="lightgray",font=("Helvatica",36),anchor=E).grid(row=0,column=1)


mainWindow.mainloop()