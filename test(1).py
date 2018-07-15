'''from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

wind = Tk()
wind.geometry("500x500")
frame = Frame(wind)
frame.pack()'''

from tkinter import *
from tkinter import messagebox
import tkinter

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
root = Tk()
mb = Menubutton(root, text = "File", font = "none 15", relief = RAISED, activebackground = "LightBlue1")

mb.menu = Menu(mb, tearoff=0, activebackground = "dodger blue4", font = "none 15")
mb["menu"] = mb.menu
mb.menu.add_command(label="New", command=donothing)
mb.menu.add_command(label="Open", command=donothing)
mb.menu.add_command(label="Save", command=donothing)
mb.menu.add_command(label="Save as...", command=donothing)
mb.menu.add_command(label="Close", command=donothing)
mb.menu.add_command(label="Exit", command=root.destroy)
#menubar.add_cascade(label="File", menu=filemenu)

#root.config(menu=menubar)
mb.grid(row = 0, column = 0)
root.mainloop()

'''A = Label(frame, text = "Try to get rid of me and bring me back.", fg = "blue")

def Toggle():
    if not A.winfo_ismapped():
        A.pack()
    elif A.winfo_ismapped():
        A.pack_forget()

def close_window():
    frame.destroy()
    
def b1():
    Button(wind, text="Toggle", width = 12, command = Toggle).pack()
frame.after(500, b1)
def b3():
    Button(wind, text="EXIT", width = 12, command = close_window).pack()
frame.after(1000, b3)
def delay(strung):
    Label(wind, text = strung, fg = "blue").pack()
x = frame.after(2000, lambda: delay("WHENEVER"))

wind.mainloop()'''
#Button(F1, text = "Browse", command = Browse).pack()
#Button(F1, text = "Search", command = lambda: Search(inFile)).pack()
