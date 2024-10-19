from tkinter import *
from tkinter.ttk import *
from time import strftime
import random

root = Tk()
root.title('Clock')
root.geometry('1000x200')

def time():
    string = strftime('%H:%M:%S %p %B %a')
    label.config(text = string)
    label.after(1500, time)

colour = ['salmon', 'green', 'purple', 'blue', 'red']

label = Label(root, font = ('Calibri', 80, 'bold'), background = random.choice(colour), foreground = 'white')
label.pack(anchor = 'center')
time()

root.mainloop()
