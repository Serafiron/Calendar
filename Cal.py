import calendar
from tkinter import *
from time import strftime
from tkcalendar import Calendar

myWindow = Tk()
root = Tk()
myWindow.title("Clock")

yy = 2023 # year
mm = 8 #month

root.geometry("400x400")

def time():
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000, time)

cal = Calendar(root, selectmode = 'day',
               year = 2023, month = 8,
               day = 25)

cal.pack(pady = 20)

def grad_date():
    date.config(text = "Selected Date is " + cal.get_date())

    Button(root, text = "Get Date",
           command = grad_date).pack(pady = 20)
    
date = Label(root, text = "")
date.pack(pady = 20)

clock = Label(myWindow, font = ('arial', 40, 'bold'),
                                background = 'dark green',
                                foreground = 'white')

clock.pack(anchor = 'center')
time()

mainloop()