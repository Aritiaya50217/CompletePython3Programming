# Event Driven Programming การเขียนโปรแกรมตามลำดับเหตุการณ์
from tkinter import *

def leftClickButton(event):
   print("Left Click !! ")

def rightClickButton(event):
    print("Right Button !! ")

def doubleClickLeft(event):
    print("DoubleClick Left !!")

def doubleClickRight(event):
    print("DoubleClick Right !!")

main = Tk()
button = Button(main,text="My Button !!")
button.place(x=40,y=20)
# <Button-1> ปุ่มซ้าย
# <Button-2> ปุ่มกลาง
# <Button-3> ปุ่มขวา
button.bind('<Button-1>',leftClickButton)
button.bind('<Button-3>',rightClickButton)
button.bind('<Double-1>',doubleClickLeft)
button.bind('<Double-3>',doubleClickRight)

main.mainloop()
