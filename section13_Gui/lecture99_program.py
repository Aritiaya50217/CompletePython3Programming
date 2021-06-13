from tkinter import *
import math


def Calculate(event) :
    result = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get())/100,2)
    print('%.2f' %result)
    # แสดงผลลัพธ์บน mainWindow
    labelResult.configure(text='%.2f' %result)

    # check BMI
    if result > 30.0:
        bmi = "อ้วนมาก"
    elif result >= 25.0 <= 29.9:
        bmi = "อ้วน"
    elif result >=23.0 <= 24.9:
        bmi = "น้ำหนักเกิน"
    elif result >= 18.6 <= 22.9 :
        bmi = "น้ำหนักปกติ เหมาะสม"
    else:
        bmi = "ผอมเกินไป"

    labelBmi.configure(text=bmi)
    print(bmi)

mainWindow = Tk()
labelHeight = Label(mainWindow,text="ส่วนสูง(cm.)").grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindow,text="น้ำหนัก(kg.)").grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(mainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',Calculate)
calculateButton.grid(row=2,column=0)

labelResult = Label(mainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

labelBmi = Label(mainWindow)
labelBmi.grid(row=2,column=2)
mainWindow.mainloop()