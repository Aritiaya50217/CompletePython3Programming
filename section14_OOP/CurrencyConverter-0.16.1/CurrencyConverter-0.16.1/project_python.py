from tkinter import *
import tkinter.font as font
import PIL
from numpy.lib.type_check import imag
import pandas
from currency_converter import *
from pandas import DataFrame 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def Currency(event):
    # ดึงข้อมูล
    data = CurrencyConverter()
    money = float(thai_entry.get())
    print("EUR Rate :",'%.2f' %data.convert(money,'THB'))
    if money <= 0 :
        result_label.configure(text="กรุณาใส่จำนวนเงิน")
    else :  
        result_label.configure(text ='%.2f' %data.convert(money,'THB'))

def LineGraph(event):
    # ข้อมูลกราฟ
    change_month = {'Month': [1,2,3,4,5,6,7,8,9,10,11,12],
            'average': [33.8082,34.1629,35.4991,35.4455,34.9527,35.077,36.0136,36.9109,36.9970,36.7955,36.0409,36.6095]
            }
    graph_data = DataFrame(change_month,columns=['Month','average'])
    # การนำกราฟมาแสดง
    figure_data = plt.Figure(figsize=(6,2), dpi=90)
    ax1 =  figure_data.add_subplot(111)
    line_data = FigureCanvasTkAgg(figure_data, line_listbox)
    line_data.get_tk_widget().pack(side=LEFT, fill=BOTH)
    graph_data = graph_data[['Month','average']].groupby('Month').sum()
    graph_data.plot(kind='line', legend=True, ax=ax1, color='r',marker='o', fontsize=10)
    ax1.set_title('Month Vs. Average Currency Rate Year 2020')

def BarGraph(event):
    # ข้อมูลกราฟ
    change_month = {'Month': [1,2,3,4,5,6,7,8,9,10,11,12],
            'average': [33.8082,34.1629,35.4991,35.4455,34.9527,35.077,36.0136,36.9109,36.9970,36.7955,36.0409,36.6095]
            }
    graph_data = DataFrame(change_month,columns=['Month','average'])

    figure_bar = plt.Figure(figsize=(6,3), dpi=90)
    ax2 = figure_bar.add_subplot(111)
    bar = FigureCanvasTkAgg(figure_bar,bar_listbox)
    bar.get_tk_widget().pack(side=LEFT, fill=BOTH)
    df1 = graph_data[['Month','average']].groupby('Month').sum()
    df1.plot(kind='bar', legend=True, ax=ax2,color = "orange")
    ax2.set_title('Month Vs. Average Currency Rate Year 2020')


def DataAgvFrame(event):
    # เปิดไฟล์ csv
    df = pandas.read_csv("Average.csv")
    print(df)
    frame_list.configure(text=df,font=Font)


mainWindow = Tk()
mainWindow.title("โปรแกรมแปลงสกุลเงิน")
mainWindow.geometry("1050x520")

#create Font object
myFont = font.Font(family='Helvetica',size=13)
Font = font.Font(size=11)

# create Label
thai_currency = Label(mainWindow,text="จำนวนเงิน (บาท)",font=myFont,fg="black")
thai_currency.place(x=20,y=25)
eur_currency = Label(mainWindow,text="จำนวนเงิน (ยูโร)",font=myFont)
eur_currency.place(x=20,y=65)
result_label = Label(mainWindow,font=myFont,fg="blue")
result_label.place(x=200,y=70)
chenge_label = Label(mainWindow,text="Average Currency Rate",font=myFont,fg="green",border=3)
chenge_label.place(x=60,y=155)

# create entry
thai_entry = Entry(mainWindow,width=20)
thai_entry.place(x=190,y=30)


# create button
check_button = Button(mainWindow,text="แปลงสกุลเงิน",font=myFont,fg="white",bg="blue")
check_button.place(x=20,y=105)
check_button.bind('<Button-1>',Currency)

line_button = Button(mainWindow,text="line Graph",font=myFont,fg="white",bg="red")
line_button.place(x=920,y=105)
line_button.bind('<Button-1>',LineGraph)

bar_button = Button(mainWindow,text="Bar Graph",font=myFont,fg="white",bg="orange")
bar_button.place(x=920,y=300)
bar_button.bind('<Button-1>',BarGraph)

data_button = Button(mainWindow,text="Data Frame",font=myFont,fg="white",bg="green")
data_button.place(x=90,y=450)
data_button.bind('<Button-1>',DataAgvFrame)

# graph
line_listbox =  Listbox(mainWindow, height=10,width=80)
line_listbox.place(x=360,y=30)

bar_listbox = Listbox(mainWindow, height=10,width=80)
bar_listbox.place(x=360,y=230)

# dataframe
frame_list = Label(mainWindow,height=15,width=30)
frame_list.place(x=10,y=180)


mainWindow.mainloop()


