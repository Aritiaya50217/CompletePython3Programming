# widget สิ่งต่าง ๆ ที่เห็นอยู่บนฟอร์มของโปรแกรม
from tkinter import *


def sayHello():
    print("Hello")

# create window
MainWindow = Tk()
# text = "ข้อความบนปุ่ม"
# command = ชื่อฟังก์ชันที่ต้องการเรียกใช้
button = Button(MainWindow,text = "Click Me",command=sayHello)
button.place(x=50,y=20)
# show window
MainWindow.mainloop()
