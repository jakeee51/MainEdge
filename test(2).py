from tkinter import *
import time

wind = Tk()
wind.geometry("250x250")
wind.config(background = "blue")
F = Frame(wind, background = "blue")
F.pack()

def load():
    symb = "—\|/"
    x = 0
    while x < 20:
        x += 1
        for item in symb:
            L1.config(text = item)
            L1.update()
            time.sleep(.1)

Button(F, text = "Get processing!", command = load).pack()
Label(F, text = "A bunch of stuff.\nThis is a test.\nFor justification.", justify = LEFT).pack()
Label(F, text = "This is just for reference.\nThis is how it does it", justify = LEFT, anchor = "w").pack()
L1 = Label(F, fg = "lime", bg = "blUE", font = "none 50")
L1.pack()
wind.mainloop()

'''import time
from tkinter import *
from tkinter import filedialog

wind = Tk()
S = Frame(wind)
S.pack()
Fr = Frame(S)
a = ['a','b','c','d']

def Show(item):
    Fr.destroy()
    Label(S, text = item).pack()

if len(a) > 1:
    Fr.pack()
    for i in a:
        print(i)
        Button(Fr, text = i, command = lambda i=i: Show(i)).pack()
        print(i)'''

'''window = Tk()
global var
global inFile
var = StringVar()
var.set("untouched")

def callback():
    inFile = filedialog.askopenfilename(filetypes =(("Text files", "*.txt"),("Comma Separated Values files","*.csv"),("All files","*.*")))
    var.set(inFile)
    
Button(window, text = "Browse", command = callback).pack()
print(var.get())
print(inFile)
window.mainloop()


def openfile():
    global filename
    filename = filedialog.askopenfilename(title="Open file")

def printfile():
    print(filename + "Used")

def printspinbox():
    print(spinbox.get())

window = Tk()

filename = "" # global variable

Button(window, text='Browse', command=openfile).pack()
Button(window, text='Print filename', command=printfile).pack()
window.mainloop()
print(filename)'''
