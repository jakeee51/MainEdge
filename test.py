<<<<<<< HEAD
from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack(side = LEFT, fill = BOTH)
scrollbar.config(command = mylist.yview)

mainloop()
#__________
'''from tkinter import *

wind = Tk()
wind.state("zoomed")

w = wind.winfo_screenwidth()
h = wind.winfo_screenheight()

sW = (wind.winfo_screenwidth() - wind.winfo_screenwidth()/2)
sH = (wind.winfo_screenheight() - wind.winfo_screenheight()/2)

xC = sW - (w/2)
yC = sH - (h/2)

photo1 = PhotoImage(file = "nypa4.png")
Label(wind, image = photo1).place(width = w, height = h, x = xC, y = yC)

wind.mainloop()'''
#__________
'''from tkinter import *
top = Tk()
top.config(bg = "#0068D0")

filename = PhotoImage(file = "nypa2.png")
background_label = Label(top, image = filename)
background_label.pack(fill = BOTH, expand = True)

top.mainloop()'''
#__________
'''import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

class mclass:
    def __init__(self,  window):
        self.window = window
        self.box = Entry(window)
        self.button = Button (window, text="check", command=self.plot)
        self.box.pack ()
        self.button.pack()

    def plot (self):
        x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
        p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
            19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])

        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.scatter(v,x,color='red')
        a.plot(p, range(2 +max(x)),color='blue')
        a.invert_yaxis()

        a.set_title ("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

window= Tk()
start= mclass(window)
window.mainloop()'''
#__________
=======
from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack(side = LEFT, fill = BOTH)
scrollbar.config(command = mylist.yview)

mainloop()
#__________
'''from tkinter import *

wind = Tk()
wind.state("zoomed")

w = wind.winfo_screenwidth()
h = wind.winfo_screenheight()

sW = (wind.winfo_screenwidth() - wind.winfo_screenwidth()/2)
sH = (wind.winfo_screenheight() - wind.winfo_screenheight()/2)

xC = sW - (w/2)
yC = sH - (h/2)

photo1 = PhotoImage(file = "nypa4.png")
Label(wind, image = photo1).place(width = w, height = h, x = xC, y = yC)

wind.mainloop()'''
#__________
'''from tkinter import *
top = Tk()
top.config(bg = "#0068D0")

filename = PhotoImage(file = "nypa2.png")
background_label = Label(top, image = filename)
background_label.pack(fill = BOTH, expand = True)

top.mainloop()'''
#__________
'''import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

class mclass:
    def __init__(self,  window):
        self.window = window
        self.box = Entry(window)
        self.button = Button (window, text="check", command=self.plot)
        self.box.pack ()
        self.button.pack()

    def plot (self):
        x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
        p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
            19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])

        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.scatter(v,x,color='red')
        a.plot(p, range(2 +max(x)),color='blue')
        a.invert_yaxis()

        a.set_title ("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

window= Tk()
start= mclass(window)
window.mainloop()'''
#__________
>>>>>>> 33e4becbe6a8b18370b59b678d1f4ea9464956dc
