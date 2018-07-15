from tkinter import *

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=1)
filemenu.add_command(label="New", font = "none 20", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=1)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()

'''from tkinter import *

master = Tk()

v = IntVar()

Radiobutton(master, text="One", variable=v, value=1).pack()
Radiobutton(master, text="Two", variable=v, value=2).pack()

mainloop()'''

'''try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the main container that holds all the frames
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        def show_1(button):
            self.frame_2.grid_remove()
            self.frame_1.show(button)

        def show_2(button):
            self.frame_1.grid_remove()
            self.frame_2.show(button)

        self.frame_1 = Page1(container, show_2)
        self.frame_2 = Page2(container, show_1)


class Page1(tk.Frame):
    def __init__(self,parent,callback):
        tk.Frame.__init__(self,parent)
        self.grid(row = 0, column = 0, sticky = "w")
        self.callback = callback

        lbl1 = tk.Label(self,text = "Yes",font =("Helvetica",12,"bold"))
        lbl1.grid(row=1,sticky="W")

        lbl2 = tk.Label(self,text = "No",font =("Helvetica",12,"bold"))
        lbl2.grid(row=1,column=1,sticky="W")

        btn1 = tk.Button(self, text="next page", font=('MS', 24, 'bold'))
        btn1.grid(row=3,column = 0,columnspan=1)

        self.var1 = tk.BooleanVar()
        rButton1 = tk.Radiobutton(self,variable = self.var1,value=True)

        rButton1.grid(row=2,sticky = "W")

        rButton2 = tk.Radiobutton(self,variable = self.var1,value=False)
        rButton2.grid(row=2,column=1,sticky = "W")

        btn1['command']= self.button_clicked

    def button_clicked(self):
        if self.var1.get():
            self.callback('button_one')
        else:
            self.callback('button_two')


class Page2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

    def show(self, selected_button):
        if selected_button == 'button_one':
            text = "This is reccomendation 2"
        elif selected_button == 'button_two':
            text = "This is reccomendation 3"
        else:
            text = selected_button
        print(selected_button)
        lbl = tk.Label(self,text=text,font=("Helvetica",12,"bold"))
        lbl.pack()
        self.grid()


app = MainApp()
app.mainloop()'''
