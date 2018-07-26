#Allow format to be customizable.
#For example, adding in fields, removing fields, editing field names and positions, and type of value within those fields. Also expecting different data patterns and being able to adjust the app to your data frame.
#Use A/B Testing for Beta.
#Add entry variables for all parameters for Beta.
'''
Author: David J. Morfe
Application Name: MainEdge
Functionality Purpose: Human Resources Manager
7/25/18
'''

#Imports and array declarations.
import time
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
departments = ["Accounting", "Business", "Development","Engineering","Human Resources","Legal","Marketing","Product","Management","Research and Development","Sales","Services","Support","Training"]
dept = ""
sex = ""

wind = Tk()
wind.state('zoomed')
wind.title("MainEdge - Human Resources Manager")
wind.config(background = "#0068D0")
MainFrame = Frame(wind, bg = "#0068D0")
MainFrame.pack()
F1 = Frame(wind, bg = "#0068D0")
F2 = Frame(wind, bg = "#0068D0")
F3 = Frame(wind, bg = "#0068D0")
MenuBar = Frame(wind, bg = "#0068D0")
MB = Menu(MenuBar, tearoff = 0)
DMB = Menu(MB, tearoff = 0)
DMB2 = Menu(MB, tearoff = 0, activebackground = "deep sky blue")

#Welcome screen.
welcome = "\n\n\n\n\n\nWELCOME TO THE HUMAN RESOURCES MANAGER APPLICATION!"
A = Label(MainFrame, font = "Helvetica 20 bold", bg = "#0068D0", fg = "gold")
A.pack()
photo1 = PhotoImage(file = "nypa4.png")
p1 = Label(MainFrame, image = photo1)
for char in welcome:
    A.config(text = A.cget('text') + char)
    A.update()
    time.sleep(.05)
p1.pack()
Label(MainFrame, text = "This application will allow you to submit an employee database file and manage it. (NOTE: File must be in .csv format)", bg = "#0068D0", fg = "white", font = "none 15").pack()
Label(MainFrame, text = "Click START to begin...", bg = "#0068D0", fg = "white", font = "none 15").pack()
def close_window():
    wind.destroy()
    exit()

def Start():
    MainFrame.destroy()
    #File uploading.
    F1.pack()
    F1.after(50, lambda: Delay(F1, "Your file is REQUIRED to match the following layout through out its contents:"))
    F1.after(100, lambda: Delay(F1, "ID,First_Name,Last_Name,Email,Gender,Department,Salary")) #Bold.
    F1.after(150, lambda: Delay(F1, "Click BROWSE and select a file to upload!"))
    F1.after(200, lambda: bDelay(F1, "BROWSE", BrowseIn))
start = Button(MainFrame, font = "none 10", text = "START", command = Start)
start.pack()

def BrowseIn():
    box = Tk()
    box.overrideredirect()
    box.withdraw()
    box.attributes("-topmost", True)
    global inFile
    inFile = filedialog.askopenfilename(filetypes =(("Text files", "*.txt"),("Comma Separated Values files","*.csv"),("All files","*.*")))
    if inFile != "":
        L1.config(text = inFile + "\nFile has been loaded!", fg = "lime", font = "none 15")
        L1.update()
        if not NextPage.winfo_ismapped():
            NextPage.pack()
    else:
        L1.config(text = "\nFailed to upload!", fg = "yellow2", font = "none 15")
        L1.update()
        if NextPage.winfo_ismapped():
            NextPage.pack_forget()
inFile = ""
L1 = Label(F1, text = "\n", bg = "#0068D0", fg = "white", font = "none 15")
L1.pack()

def Delay(page, strung):
    Label(page, text = strung, bg = "#0068D0", fg = "white", font = "none 15").pack()
def bDelay(page, strung, cmd):
    Button(page, font = "none 10", text = strung, command = cmd).pack()

def BrowsePage():
    F1.destroy()
    F2.pack()
NextPage = Button(F1, font = "none 10", text = "NEXT", command = BrowsePage)

def BrowseOut():
    box = Tk()
    box.overrideredirect()
    box.withdraw()
    box.attributes("-topmost", True)
    global outFile
    outFile = filedialog.askopenfilename(filetypes =(("Text files", "*.txt"),("Comma Separated Values files","*.csv"),("All files","*.*")))
    if "RENAME_ME" in outFile:
        L2.config(text = "Warning, cannot upload this file! Rename the file as it is stated or try a different file!")
        L2.update()
        if NextPage1.winfo_ismapped():
            NextPage1.pack_forget()
    elif outFile != "":
        L2.config(text = outFile + "\nArchive file has been loaded!", fg = "lime", font = "none 15")
        L2.update()
        if not NextPage1.winfo_ismapped():
            NextPage1.pack()
    else:
        L2.config(text = "\nFailed to upload!", fg = "yellow2", font = "none 15")
        L2.update()
        if NextPage1.winfo_ismapped():
            NextPage1.pack_forget()
outFile = ""
L2 = Label(F3, text = "\n", bg = "#0068D0", fg = "white", font = "none 15")
L2.pack()

Label(F2, text = "Do you have an archive file?", bg = "#0068D0", fg = "white", font = "none 15").pack()
def YesOut():
    F2.destroy()
    F3.pack()
    F3.after(50, lambda: Delay(F3, "Please upload an archive file now. File MUST match the following format throughout its contents:"))
    F3.after(100, lambda: Delay(F3, "ID,First_Name,Last_Name,Email,Gender,Department,Salary,Status"))
    F3.after(150, lambda: Delay(F3, "NOTE: 'Status' field may either be 'Fired','Quit' or 'LayOff'."))
    F3.after(200, lambda: Delay(F3, "Click BROWSE and select an archive file to upload!"))
    F3.after(250, lambda: bDelay(F3, "BROWSE", BrowseOut))
def NoOut():
    global outFile
    F2.destroy()
    F3.pack()
    F3.after(50, lambda: Delay(F3, "That's ok! A new file will now be created for you in the location you ran this program. It will be called 'RENAME_ME.txt'."))
    F3.after(100, lambda: Delay(F3, "This is so that employees you remove with this program get their employee information stored for later reference."))
    F3.after(150, lambda: Delay(F3, "Be sure to RENAME this file when you exit the program, to upload for later use! Otherwise this file may be accidentally overwritten!"))
    outFile = open("RENAME_ME.txt", "w")
    outFile.write("ID,First_Name,Last_Name,Email,Gender,Department,Salary,Status\n")
    outFile.close()
    outFile = "RENAME_ME.txt"
    NextPage1.pack()
yOut = Button(F2, width = 4, font = "none 10", text = "YES", command = YesOut)
yOut.pack()
nOut = Button(F2, width = 4, font = "none 10", text = "NO", command = NoOut)
nOut.pack()

def Upload():
    #Return to upload screen.
    wind.config(menu = "")
    MenuBar.pack_forget()
    U = Frame(wind, bg = "#0068D0")
    U.pack()
    Button(U, font = "none 10", text="MENU", width = 12, command = lambda: RTM(U)).pack(side = BOTTOM)
    UE = Frame(U, bg = "#0068D0")
    UP = Frame(U, bg = "#0068D0")
    UE.pack(side = TOP)
    UP.pack(side = BOTTOM)
    def RBrowseIn():
        box = Tk()
        box.overrideredirect()
        box.withdraw()
        box.attributes("-topmost", True)
        global inFile
        inFile = filedialog.askopenfilename(filetypes =(("Text files", "*.txt"),("Comma Separated Values files","*.csv"),("All files","*.*")))
        if inFile != "":
            LE.config(text = inFile + "\nFile has been loaded!", fg = "lime", font = "none 15")
            LE.update()
            FStat.config(text = "Employee File: " + inFile + "\nArchive File: " + outFile, fg = "spring green", font = "none 11")
            FStat.update()
            if outFile == "":
                FStat.config(text = "Employee File: " + inFile + "\nWARNING: Archive file missing!", fg = "yellow2", font = "none 11")
                FStat.update()
        elif inFile == "" and outFile == "":
            FStat.config(text = "WARNING: Employee file missing!" + "\nWARNING: Archive file missing!" + outFile, fg = "yellow2", font = "none 11")
            FStat.update()
            LP.config(text = "Failed to upload!", fg = "yellow2", font = "none 15")
            LP.update()
            LE.config(text = "Failed to upload!", fg = "yellow2", font = "none 15")
            LE.update()
        else:
            LE.config(text = "Failed to upload!", fg = "yellow2", font = "none 15")
            LE.update()
            FStat.config(text = "WARNING: Employee file missing!" + "\nArchive File: " + outFile, fg = "yellow2", font = "none 11")
            FStat.update()
    def RBrowseOut():
        box = Tk()
        box.overrideredirect()
        box.withdraw()
        box.attributes("-topmost", True)
        global outFile
        outFile = filedialog.askopenfilename(filetypes =(("Text files", "*.txt"),("Comma Separated Values files","*.csv"),("All files","*.*")))
        if "RENAME_ME" in outFile:
            LP.config(text = "Warning, cannot upload this file! Rename the file as it is stated or try a different file!")
            LP.update()
        elif outFile != "":
            LP.config(text = outFile + "\nArchive file has been loaded!", fg = "lime", font = "none 15")
            LP.update()
            FStat.config(text = "Employee File: " + inFile + "\nArchive File: " + outFile, fg = "spring green", font = "none 11")
            FStat.update()
            if inFile == "":
                FStat.config(text = "WARNING: Employee file missing!" + "\nArchive File: " + outFile, fg = "yellow2", font = "none 11")
                FStat.update()
        elif inFile == "" and outFile == "":
            FStat.config(text = "WARNING: Employee file missing!" + "\nWARNING: Archive file missing!" + outFile, fg = "yellow2", font = "none 11")
            FStat.update()
            LE.config(text = "Failed to upload!", fg = "yellow2", font = "none 15")
            LE.update()
            LP.config(text = "Failed to upload!", fg = "yellow2", font = "none 15")
            LP.update()
        else:
            LP.config(text = "Failed to upload!", fg = "yellow2", font = "none 15")
            LP.update()
            FStat.config(text = "Employee File: " + inFile + "\nWARNING: Archive file missing!", fg = "yellow2", font = "none 11")
            FStat.update()
    LE = Label(UE, bg = "#0068D0", fg = "white", font = "none 15")
    LE.pack()
    LP = Label(UP, bg = "#0068D0", fg = "white", font = "none 15")
    LP.pack()
    Button(UE, font = "none 10", text = "BROWSE", command = RBrowseIn).pack()
    Button(UP, font = "none 10", text = "BROWSE", command = RBrowseOut).pack()
    Label(UE, text = "Please upload an employee file with the following format:\nID,First_Name,Last_Name,Email,Gender,Department,Salary", bg = "#0068D0", fg = "white", font = "none 15").pack()
    Label(UP, text = "Please upload an archive file with the following format:\nID,First_Name,Last_Name,Email,Gender,Department,Salary,Status", bg = "#0068D0", fg = "white", font = "none 15").pack()

#Library features.
def Check(employee):
    result = messagebox.askquestion("Check yourself!", "Is this the correct employee?\n" + employee, icon='question')
    if result == 'yes':
        return True
    else:
        return False

def Search(inFile):
    wind.config(menu = "")
    MenuBar.pack_forget()
    S = Frame(wind, bg = "#0068D0")
    S.pack()
    Fr = Frame(S)
    s = Label(S, text = "Enter employee's attribute:", bg = "#0068D0", fg = "white", font = "none 15")
    s.pack()
    def ShoSe(frm,employee):
        y = Label(bg = "#0068D0", fg = "white", font = "none 15")
        if not y.winfo_ismapped():
            lst = employee.split(',')
            x = "ID-\t\t{}\nName-\t\t{} {}\nEmail-\t\t{}\nGender-\t\t{}\nDepartment-\t{}\nSalary-\t\t${}".format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6])
            y = Label(frm, text = x, justify = LEFT, fg = "lime", font = "none 15", bg = "#0068D0")
            y.pack()
            s.destroy()
    def Shorb(employee):
        Fr.destroy()
        lst = employee.split(',')
        x = "ID-\t\t{}\nName-\t\t{} {}\nEmail-\t\t{}\nGender-\t\t{}\nDepartment-\t{}\nSalary-\t\t${}".format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6])
        y = Label(S, text = x, justify = LEFT, fg = "lime", font = "none 15", bg = "#0068D0")
        y.pack()
        a.destroy()
        s.destroy()
    def get(inFile):
        z = 0
        temp = []
        v = StringVar()
        x = "Searching"
        chk = ""
        while z < 3:
            z += 1
            x = x + "."
            b.config(text = x, fg = "white", font = "none 15")
            b.update()
            time.sleep(.25)
        global g
        g = a.get()
        a.delete(0, END)
        g = g.lower()
        with open(inFile) as f:
            line = f.readline()
            while True:
                line = f.readline()
                if line == "":
                    if len(temp) > 1:
                        Fr.pack()
                        a.destroy()
                        for emp in temp:
                            RB = Radiobutton(Fr, variable = v, value = emp, text = emp, height = 2, overrelief = SUNKEN, indicatoron = 0, command = lambda emp=emp: Shorb(emp))
                            RB.pack()
                    if chk == False:
                        b.config(text = "Not what you're looking for? Please try agin.", fg = "yellow2", font = "none 15")
                        b.update()
                        break
                    if chk == True:
                        b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                        b.update()
                        break
                    if len(temp) == 0:
                        b.config(text = "Employee not found! Please try again.", fg = "yellow2", font = "none 15")
                        b.update()
                        break
                    if len(temp) == 1:
                        s.config(text = "Enter employee's attribute:", fg = "white", font = "none 15")
                        s.update()
                        chk = Check(temp[0])
                        if chk == True:
                            ShoSe(S, temp[0])
                            a.destroy()
                        else:
                            F.pack()
                            b.config(text = "Not what you're looking for? Please try agin.", fg = "yellow2", font = "none 15")
                            b.update()

                    break
                emp = line.split(',')
                emply = [emp[0],emp[3]]
                first = emp[1]
                last = emp[2]
                name = first + " " + last
                if g in emply:
                    for atr in emply:
                        if g == atr.lower():
                            b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                            b.update()
                            F.pack_forget()
                            chk = Check(line)
                            if chk == True:
                                ShoSe(S,line)
                                a.destroy()
                            else:
                                b.config(text = "")
                                b.update()
                                F.pack()
                elif g == name.lower():
                    b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                    b.update()
                    F.pack_forget()
                    chk = Check(line)
                    if chk == True:
                        ShoSe(S,line)
                        a.destroy()
                    else:
                        b.config(text = "")
                        b.update()
                        F.pack()
                elif g == first.lower():
                    b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                    b.update()
                    temp.append(line)
                    F.pack_forget()
                    s.config(text = "Select the employee:", fg = "lime", font = "none 15")
                    s.update()
                    #List of all with that name.
                elif g == last.lower():
                    b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                    b.update()
                    temp.append(line)
                    F.pack_forget()
                    s.config(text = "Select the employee:", fg = "lime", font = "none 15")
                    s.update()
                    #List of all with that name.
    a = Entry(S, font = "none 12")
    a.pack()
    b = Label(S, bg = "#0068D0", fg = "white", font = "none 15")
    b.pack()
    F = Button(S, font = "none 10", text = "FIND", command = lambda: get(inFile))
    F.pack()
    Button(S, font = "none 10", text="MENU", width = 12, command = lambda: RTM(S)).pack(side = BOTTOM)

def Hire(inFile,outFile):
    wind.config(menu = "")
    MenuBar.pack_forget()
    Fr = Frame(wind, bg = "#0068D0")
    Fr.pack()
    H = Frame(Fr, bg = "#0068D0")
    H.pack()
    BH = Frame(Fr, bg = "#0068D0")
    BH.pack(side = TOP)
    file1 = open(inFile)
    file2 = open(outFile) #Blacklisted & other previous employees file.
    readFile = file1.readlines()
    BLF = file2.readlines()
    #ID number availability checker.
    lastEmp = readFile[-1]
    lastEmply = lastEmp.split(',')
    newID = int(lastEmply[0])
    newID += 1
    for emp in BLF:
        emp = emp.strip('\n')
        emply = emp.split(',')
        if emply[0] == "ID":
            continue
        elif newID == int(emply[0]):
            newID += 1
            break
        else:
            break
    def Select(unit):
        global dept
        dept = unit
        RB.config(text = dept)
        RB.update()
        L6.config(text = "")
        L6.update()
    x = 0
    y = 0
    for item in departments:
        Button(BH, font = "none 10", text = item, command = lambda item=item: Select(item)).grid(row = x, column = y, sticky = W+E)#Organize buttons into square.
        if x < 4:
            x += 1
        elif x == 4:
            y += 1
            x = 0
    def Male():
        global sex
        sex = "Male"
        L4.config(text = "")
        L4.update()
    def Female():
        global sex
        sex = "Female"
        L4.config(text = "")
        L4.update()
    #Submit button.
    def get(inFile,outFile):
        first = F.get()
        last = L.get()
        email = Em.get()
        sal = S.get()
        phase = 0
        done = 0
        #Name checker.
        if len(first) > 20 or first == "" or first[-1] == " " or first.isdigit():
            L1.config(text = "Invalid input! Only 20 characters max and no trailing spaces allowed!")
            L1.update()
        else:
            L1.config(text = "")
            L1.update()
            phase += 1
            done += 1
        if len(last) > 20 or last == "" or last[-1] == " "or last.isdigit():
            L2.config(text = "Invalid input! Only 20 characters max and no trailing spaces allowed!")
            L2.update()
        else:
            L2.config(text = "")
            L2.update()
            phase += 1
            done += 1
        #For loop below checks if name is in previous AND blacklisted.
        first = first.capitalize()
        last = last.capitalize()
        email = email.lower()
        rtn = True
        Qui = 0
        Lay = 0
        if phase == 2:
            for emp in BLF:
                emp = emp.strip('\n')
                emply = emp.split(',')
                if first == emply[1] and last == emply[2] and "Fired" == emply[-1]:
                    rtn = False
                elif first == emply[1] and last == emply[2] and "Quit" == emply[-1]:
                    rtn = True
                    Qui += 1
                elif first == emply[1] and last == emply[2] and "LayOff" == emply[-1]:
                    rtn = True
                    Lay += 1
            if Qui == 1:
                RES.config(text = "Welcome back " + first + " " + last + "! Don't leave us again.")
                RES.update()
            elif Lay == 1:
                RES.config(text = "Heh, yea sorry about that. Glad to have you back " + first + " " + last + "!")
                RES.config()
            else:
                RES.config(text = "")
                RES.update()
        if rtn:
            RES.config(text = "")
            RES.update()
            #Email checker.
            if "@" not in email or "." not in email:
                L3.config(text = "This email is invalid! Please try again.")
                L3.update()
            elif len(email) > 28:
                L3.config(text = "This email is too long!")
                L3.update()
            else:
                L3.config(text = "")
                L3.update()
                done += 1
            #Gender checker.
            if sex == "":
                L4.config(text = "Please select a gender!")
                L4.update()
            else:
                done += 1
            #Department checker.
            if dept == "":
                L6.config(text = "Please select a department!")
                L6.update()
            else:
                done += 1
            #Salary checker.
            try:
                sal = int(sal)
            except ValueError:
                L5.config(text = "Must be an integer!")
                L5.update()
            try:
                if sal < 50000 or sal > 100000:
                    L5.config(text = "Oh no! You must choose a salary between $50,000 and $100,000.")
                    L5.update()
                else:
                    L5.config(text = "")
                    L5.update()
                    done += 1
            except TypeError:
                L5.config(text = "Must be an integer!")
                L5.update()
        else:
            RES.config(text = "I don't think so! Person has been blacklisted!")
            RES.update()
        #Compile & insert all inputed fields.
        if done == 6:
            H.destroy()
            BH.destroy()
            file3 = open(inFile,"a")
            file3.write("\n{},{},{},{},{},{},{}".format(newID,first,last,email,sex,dept,sal))
            Label(Fr, fg = "lime", font = "none 15", justify = LEFT, text = "\n\n\n\n\n\n\n\n\n{} {} has been added into the employee database with the following attributes:\nID- {}\nEmail- {}\nGender- {}\nDepartment- {}\nSalary- ${}".format(first,last,newID,email,sex,dept,sal), bg = "#0068D0").pack()
            file3.close()
    file1.close()
    file2.close()

    #First
    Label(H, text = "Enter employee's first name:", bg = "#0068D0", fg = "white", font = "none 15").grid(row = 0, sticky=W)
    F = Entry(H, width = 28, font = "none 12")
    F.grid(row = 0, column = 1)
    L1 = Label(H, fg = "yellow2", font = "none 15", bg = "#0068D0")#Error message.
    L1.grid(row = 1, columnspan = 2, sticky=W)
    #Last
    Label(H, text = "Enter employee's last name:", bg = "#0068D0", fg = "white", font = "none 15").grid(row = 2, sticky=W)
    L = Entry(H, width = 28, font = "none 12")
    L.grid(row = 2, column = 1)
    L2 = Label(H, fg = "yellow2", font = "none 15", bg = "#0068D0")#Error message.
    L2.grid(row = 3, columnspan = 2, sticky=W)
    #Email
    Label(H, text = "Enter employee's email:", bg = "#0068D0", fg = "white", font = "none 15").grid(row = 4, sticky=W)
    Em = Entry(H, width = 28, font = "none 12")
    Em.grid(row = 4, column = 1)
    L3 = Label(H, fg = "yellow2", font = "none 15", bg = "#0068D0")#Error message.
    L3.grid(row = 5, columnspan = 2, sticky=W)
    #Gender
    v = StringVar()
    Label(H, text = "Enter employee's biological sex:", bg = "#0068D0", fg = "white", font = "none 15").grid(row = 6, sticky=W)
    Radiobutton(H, variable = v, value = 1, text = "MALE", font = "none 10", command = Male).grid(row = 6, column = 1, sticky=E)
    Radiobutton(H, variable = v, value = 2, text = "FEMALE", font = "none 10", command = Female).grid(row = 6, column = 2, sticky=W)
    L4 = Label(H, fg = "yellow2", font = "none 15", bg = "#0068D0")#Error message.
    L4.grid(row = 7, columnspan = 2, sticky=W)
    #Salary
    Label(H, text = "Enter a salary:", bg = "#0068D0", fg = "white", font = "none 15").grid(row = 8, sticky=W)
    S = Entry(H, width = 28, font = "none 12")
    S.grid(row = 8, column = 1)
    L5 = Label(H, fg = "yellow2", font = "none 15", bg = "#0068D0")#Error message.
    L5.grid(row = 9, columnspan = 2, sticky=W)
    #Department
    Label(H, text = "Enter the department that hired you:", bg = "#0068D0", fg = "white", font = "none 15").grid(row = 10, sticky=W)
    RB = Label(H, fg = "blue", relief = RIDGE, width = 24, font = "none 12")
    RB.grid(row = 10, column = 1)
    L6 = Label(H, fg = "yellow2", font = "none 15", bg = "#0068D0")#Error message.
    L6.grid(row = 11, columnspan = 2, sticky=W)

    Button(H, font = "none 10", text = "SUBMIT", command = lambda: get(inFile,outFile)).grid(row = 13, columnspan = 3, sticky = N)
    Button(Fr, font = "none 10", text = "MENU", width = 12, command = lambda: RTM(Fr)).pack(side = BOTTOM)
    RES = Label(H, fg = "lime", font = "none 15", bg = "#0068D0")
    RES.grid(row = 12, columnspan = 2, sticky=E)

def Quit(inFile, outFile):
    wind.config(menu = "")
    MenuBar.pack_forget()
    Q = Frame(wind, bg = "#0068D0")
    Q.pack()
    file1 = open(inFile, "r")
    file2 = open(outFile, "a")
    readFile = file1.readlines()
    def get(inFile,outFile):
        IDN = idn.get()
        chk = ""
        if len(IDN) != 4 or not IDN.isnumeric:
            L1.config(text = "Input invalid! Please enter the [4 digit ID] of the employee you want to remove.", fg = "yellow2", font = "none 9")
            L1.update()
        else:
            x = 0
            symb = "—\|/"
            while x < 10:
                for item in symb:
                    x += 1
                    L1.config(text = item, fg = "lime", font = "none 15")
                    L1.update()
                    time.sleep(.1)
            fnd = ""
            for emp in readFile:
                emp = emp.strip('\n')
                emply = emp.split(',')
                if IDN == emply[0]:
                    fnd = "found"
                    L1.config(text ="", font = "none 9")
                    L1.update()
                    chk = Check(emp)
                    break
            if fnd == "":
                L1.config(text = "Employee not found! Use the 'Search' feature if this persists.", fg = "yellow2", font = "none 9")
                L1.update()
        if chk == True:
            for emp in readFile:
                emp = emp.strip('\n')
                emply = emp.split(',')
                if IDN == emply[0]:
                    L1.config(fg = "yellow2", text = "{} {} has been removed from the system.\nThe employee has also been added into the '{}' file.".format(emply[1],emply[2],outFile), font = "none 9")
                    file2.write('\n' + emp + ',Quit')
                    file2.close()
                    QR.destroy()
                    idn.destroy()
            file4 = open(inFile, "w")
            head = readFile.pop(0)
            head = head.strip('\n')
            file4.write(head)
            for emp in readFile:
                emp = emp.strip('\n')
                emply = emp.split(',')
                if IDN != emply[0]:
                    file4.write('\n' + emp)
            file4.close()

    Label(Q, text = "Enter the ID # of the employee you want to remove from the system:", bg = "#0068D0", fg = "white", font = "none 15").pack()
    idn = Entry(Q, font = "none 12")
    idn.pack()
    L1 = Label(Q, bg = "#0068D0", fg = "white", font = "none 15")
    L1.pack()

    QR = Button(Q, font = "none 10", text = "RETIRE", command = lambda: get(inFile,outFile))
    QR.pack()
    Button(Q, font = "none 10", text = "MENU", width = 12, command = lambda: RTM(Q)).pack(side = BOTTOM)

def Fire(inFile, outFile):
    wind.config(menu = "")
    MenuBar.pack_forget()
    F = Frame(wind, bg = "#0068D0")
    F.pack()
    file1 = open(inFile, "r")
    file2 = open(outFile, "a")
    readFile = file1.readlines()
    def get(inFile,outFile):
        IDN = idn.get()
        chk = ""
        if len(IDN) != 4 or not IDN.isnumeric:
            L1.config(text = "Input invalid! Please enter the [4 digit ID] of the employee you want to TERMINATE.", fg = "yellow2", font = "none 9")
            L1.update()
        else:
            x = 0
            symb = "—\|/"
            while x < 10:
                for item in symb:
                    x += 1
                    L1.config(text = item, fg = "lime", font = "none 15")
                    L1.update()
                    time.sleep(.1)
            fnd = ""
            for emp in readFile:
                emp = emp.strip('\n')
                emply = emp.split(',')
                if IDN == emply[0]:
                    fnd = "found"
                    L1.config(text ="", font = "none 9")
                    L1.update()
                    chk = Check(emp)
                    break
            if fnd == "":
                L1.config(text = "Employee not found! Use the 'Search' feature if this persists.", fg = "yellow2", font = "none 9")
                L1.update()
        if chk == True:
            for emp in readFile:
                emp = emp.strip('\n')
                emply = emp.split(',')
                if IDN == emply[0]:
                    L1.config(fg = "yellow2", text = "{} {} has been blacklisted & TERMINATED from the system.\nThe employee has also been added into the '{}' file.".format(emply[1],emply[2],outFile), font = "none 9")
                    file2.write('\n' + emp + ',Fired')
                    file2.close()
                    FR.destroy()
                    idn.destroy()
            file4 = open(inFile, "w")
            head = readFile.pop(0)
            head = head.strip('\n')
            file4.write(head)
            for emp in readFile:
                emp = emp.strip('\n')
                emply = emp.split(',')
                if IDN != emply[0]:
                    file4.write('\n' + emp)
            file4.close()

    Label(F, text = "Enter the ID # of the employee you want to TERMINATE from the system:", bg = "#0068D0", fg = "white", font = "none 15").pack()
    idn = Entry(F, font = "none 12")
    idn.pack()
    L1 = Label(F, bg = "#0068D0", fg = "white", font = "none 15")
    L1.pack()

    FR = Button(F, font = "none 10", text = "RETIRE", command = lambda: get(inFile,outFile))
    FR.pack()
    Button(F, font = "none 10", text = "MENU", width = 12, command = lambda: RTM(F)).pack(side = BOTTOM)

def LayOff(inFile, outFile):
    wind.config(menu = "")
    MenuBar.pack_forget()
    LO = Frame(wind, bg = "#0068D0")
    LO.pack()
    file1 = open(inFile, "r")
    file2 = open(outFile, "a")
    readFile = file1.readlines()
    def get(inFile,outFile):
        IDN = idn.get()
        chk = ""
        if len(IDN) != 4 or not IDN.isnumeric:
            L1.config(text = "Input invalid! Please enter the [4 digit ID] of the employee you want to DELETE.", fg = "yellow2", font = "none 9")
            L1.update()
        else:
            x = 0
            symb = "—\|/"
            while x < 10:
                for item in symb:
                    x += 1
                    L1.config(text = item, fg = "lime", font = "none 15")
                    L1.update()
                    time.sleep(.1)
            fnd = ""
            for emp in readFile:
                emp = emp.strip('\n')
                emply = emp.split(',')
                if IDN == emply[0]:
                    fnd = "found"
                    L1.config(text ="", font = "none 9")
                    L1.update()
                    chk = Check(emp)
                    break
            if fnd == "":
                L1.config(text = "Employee not found! Use the 'Search' feature if this persists.", fg = "yellow2", font = "none 9")
                L1.update()
        if chk == True:
            for emp in readFile:
                emp = emp.strip('\n')
                emply = emp.split(',')
                if IDN == emply[0]:
                    L1.config(fg = "yellow2", text = "{} {} has been DELETED from the system.\nThe employee has also been added into the '{}' file.".format(emply[1],emply[2],outFile), font = "none 9")
                    file2.write('\n' + emp + ',LayOff')
                    file2.close()
                    LR.destroy()
                    idn.destroy()
            file4 = open(inFile, "w")
            head = readFile.pop(0)
            head = head.strip('\n')
            file4.write(head)
            for emp in readFile:
                emp = emp.strip('\n')
                emply = emp.split(',')
                if IDN != emply[0]:
                    file4.write('\n' + emp)
            file4.close()

    Label(LO, text = "Enter the ID # of the employee being laid off:", bg = "#0068D0", fg = "white", font = "none 15").pack()
    idn = Entry(LO, font = "none 12")
    idn.pack()
    L1 = Label(LO, bg = "#0068D0", fg = "white", font = "none 15")
    L1.pack()

    LR = Button(LO, font = "none 10", text = "Lay Off", command = lambda: get(inFile,outFile))
    LR.pack()
    Button(LO, font = "none 10", text = "MENU", width = 12, command = lambda: RTM(LO)).pack(side = BOTTOM)

def Promote(inFile):
    wind.config(menu = "")
    MenuBar.pack_forget()
    P = Frame(wind, bg = "#0068D0")
    P.pack()
    Fr = Frame(P)
    s = Label(P, text = "Enter an attribute of the employee you wish to promote:", bg = "#0068D0", fg = "white", font = "none 15")
    s.pack()
    def Show(frm,employee):
        y = Label(bg = "#0068D0", fg = "white", font = "none 15")
        if not y.winfo_ismapped():
            lst = employee.split(',')
            x = "ID-\t\t{}\nName-\t\t{} {}\nEmail-\t\t{}\nGender-\t\t{}\nDepartment-\t{}\nSalary-\t\t${}".format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6])
            y = Label(frm, text = x, justify = LEFT, fg = "lime", font = "none 15", bg = "#0068D0")
            y.pack()
            a.destroy()
            s.destroy()
            global ge
            ge = employee
            p.pack()
    def Shorb(employee):
        Fr.destroy()
        lst = employee.split(',')
        x = "ID-\t\t{}\nName-\t\t{} {}\nEmail-\t\t{}\nGender-\t\t{}\nDepartment-\t{}\nSalary-\t\t${}".format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6])
        y = Label(P, text = x, justify = LEFT, fg = "lime", font = "none 15", bg = "#0068D0")
        y.pack()
        a.destroy()
        s.destroy()
        global ge
        ge = employee
        p.pack()
    def Promo(frm,employee):
        frm.destroy()
        Pr = Frame(wind, bg = "#0068D0")
        Pr.pack()
        L1 = Label(Pr, fg = "yellow2", font = "none 15", bg = "#0068D0")
        L1.pack()
        Button(Pr, font = "none 10", text="MENU", width = 12, command = lambda: RTM(Pr)).pack(side = BOTTOM)
        with open(inFile, "r") as f:
            line = f.readline()
            while line != "":
                line = f.readline()
                if employee in line:
                    line = line.split(',')
                    salOld = int(line.pop(-1))
                    salRaise = salOld * .02
                    salNew = int(salOld + salRaise)
                    if salOld == 100000:
                        L1.config(text = "Warning: Employee has already reached the maximum salary of $100,000!")
                        L1.update()
                        salNew = 100000
                    elif salNew > 100000:
                        L1.config(text = "Employee has reached the maximum salary of $100,000!")
                        L1.update()
                        salNew = 100000
                    else:
                        salNewStr = str(salNew)
                        emp = "Congratulations! " + line[1] + " " + line[2] + " has been promoted with a current salary of $" + salNewStr
                        L1.config(text = emp, fg = "lime", font = "none 15")
                        L1.update()
                    getLine = ','.join(line)
                    getLine = getLine.strip("\n")
                    newLine = getLine + "," + str(salNew)
        file1 = open(inFile)
        lines = file1.readlines()
        file1.close()
        file2 = open(inFile, "w")
        for employee in lines:
            employee = employee.strip("\n")
            if employee in lines[0]:
                file2.write(employee)
            elif getLine in employee:
                file2.write("\n" + newLine)
            else:
                file2.write("\n" + employee)
        file2.close()
    def get(inFile):
        z = 0
        temp = []
        v = StringVar()
        x = "Searching"
        chk = ""
        while z < 3:
            z += 1
            x = x + "."
            b.config(text = x, fg = "white", font = "none 15")
            b.update()
            time.sleep(.25)
        global gee
        gee = a.get()
        a.delete(0, 'end')
        g = gee.lower()
        with open(inFile) as f:
            line = f.readline()
            while True:
                line = f.readline()
                if line == "":
                    if len(temp) > 1:
                        Fr.pack()
                        a.destroy()
                        for emp in temp:
                            RB = Radiobutton(Fr, variable = v, value = emp, text = emp, height = 2, overrelief = SUNKEN, indicatoron = 0, command = lambda emp=emp: Shorb(emp))
                            RB.pack()
                    if chk == False:
                        b.config(text = "Not what you're looking for? Please try agin.", fg = "yellow2", font = "none 15")
                        b.update()
                        break
                    if chk == True:
                        b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                        b.update()
                        break
                    if len(temp) == 0:
                        b.config(text = "Employee not found! Please try again.", fg = "yellow2", font = "none 15")
                        b.update()
                        break
                    if len(temp) == 1:
                        s.config(text = "Enter an attribute of the employee you wish to promote:", fg = "white", font = "none 15")
                        s.update()
                        chk = Check(temp[0])
                        if chk == True:
                            Show(P, temp[0])
                        else:
                            F.pack()
                            b.config(text = "Not what you're looking for? Please try agin.", fg = "yellow2", font = "none 15")
                            b.update()
                    break
                emp = line.split(',')
                emply = [emp[0],emp[3]]
                first = emp[1]
                last = emp[2]
                name = first + " " + last
                if g in emply:
                    for atr in emply:
                        if g == atr.lower():
                            b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                            b.update()
                            F.pack_forget()
                            chk = Check(line)
                            if chk == True:
                                Show(P,line)
                            else:
                                b.config(text = "")
                                b.update()
                                F.pack()
                elif g == name.lower():
                    b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                    b.update()
                    F.pack_forget()
                    chk = Check(line)
                    if chk == True:
                        Show(P,line)
                    else:
                        b.config(text = "")
                        b.update()
                        F.pack()
                elif g == first.lower():
                    b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                    b.update()
                    temp.append(line)
                    F.pack_forget()
                    s.config(text = "Select the employee:", fg = "lime", font = "none 15")
                    s.update()
                elif g == last.lower():
                    b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                    b.update()
                    temp.append(line)
                    F.pack_forget()
                    s.config(text = "Select the employee:", fg = "lime", font = "none 15")
                    s.update()
    a = Entry(P, font = "none 12")
    a.pack()
    b = Label(P, bg = "#0068D0", fg = "white", font = "none 15")
    b.pack()
    p = Button(P, font = "none 10", text = "Promote", command = lambda: Promo(P,ge))
    F = Button(P, font = "none 10", text = "FIND", command = lambda: get(inFile))
    F.pack()
    Button(P, font = "none 10", text="MENU", width = 12, command = lambda: RTM(P)).pack(side = BOTTOM)

def Change(inFile):
    wind.config(menu = "")
    MenuBar.pack_forget()
    C = Frame(wind, bg = "#0068D0")
    C.pack()
    Fr = Frame(C, bg = "#0068D0")
    s = Label(C, text = "Enter an attribute of the employee who's attribute needs updating:", bg = "#0068D0", fg = "white", font = "none 15")
    s.pack()
    def Show(frm,employee):
        y = Label(bg = "#0068D0", fg = "white", font = "none 15")
        if not y.winfo_ismapped():
            lst = employee.split(',')
            x = "ID-\t\t{}\nName-\t\t{} {}\nEmail-\t\t{}\nGender-\t\t{}\nDepartment-\t{}\nSalary-\t\t${}".format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6])
            y = Label(frm, text = x, justify = LEFT, fg = "lime", font = "none 15", bg = "#0068D0")
            y.pack()
            global ge
            ge = employee
            c.pack()
            a.destroy()
            s.destroy()
    def Shorb(employee):
        Fr.destroy()
        lst = employee.split(',')
        x = "ID-\t\t{}\nName-\t\t{} {}\nEmail-\t\t{}\nGender-\t\t{}\nDepartment-\t{}\nSalary-\t\t${}".format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6])
        y = Label(C, text = x, justify = LEFT, fg = "lime", font = "none 15", bg = "#0068D0")
        y.pack()
        global ge
        ge = employee
        c.pack()
        a.destroy()
        s.destroy()
    def Chang(frm,employee):
        frm.destroy()
        Ch = Frame(wind, bg = "#0068D0")
        Ch.pack()
        Button(Ch, font = "none 10", text="MENU", width = 12, command = lambda: RTM(Ch)).pack(side = BOTTOM)
        Fr = Frame(Ch, bg = "#0068D0")
        Fr.pack()
        def Select(frm,employee):
            frm.destroy()
            Sel = Frame(Ch, bg = "#0068D0")
            Sel.pack()
            def Update(CA):
                def CC(CA):
                    g = CA.get()
                    if "@" in employee:
                        if len(g) > 30:
                            Err.config(text = "Email can't be over 30 characters!")
                            Err.update()
                            CA.delete(0, END)
                            CA.insert(0, employee)
                            return False
                        elif "@" not in g or "." not in g or g == "" or g[-1] == " ":
                            Err.config(text = "Invalid email! Try again.")
                            Err.update()
                            CA.delete(0, END)
                            CA.insert(0, employee)
                            return True
                    if len(g) > 20:
                        Err.config(text = "Name can't be over 20 characters!")
                        Err.update()
                        CA.delete(0, END)
                        CA.insert(0, employee)
                        return False
                    elif g == "" or g[-1] == " ":
                        Err.config(text = "Invalid input! No trailing spaces allowed!")
                        Err.update()
                        CA.delete(0, END)
                        CA.insert(0, employee)
                        return False
                    else:
                        return True
                a = CC(CA)
                new = CA.get()
                prev = employee
                if a == True:
                    E.destroy()
                    U.destroy()
                    H.config(text = "Employee attribute has been updated!\n{} ---> {}".format(prev,new), fg = "lime", font = "none 15")
                    H.update()
                    f = open(inFile)
                    lines = f.readlines()
                    f.close()
                    with open(inFile, "w") as f1:
                        for line in lines:
                            if prev in line:
                                line = line.replace(prev, new)
                                f1.write(line)
                            else:
                                f1.write(line)
            H = Label(Sel, text = "Update the atttribute:", bg = "#0068D0", fg = "white", font = "none 15")
            H.pack()
            E = Entry(Sel, relief = RAISED, width = 30, font = "none 12")
            E.pack()
            E.insert(0, employee)
            Err = Label(Sel, fg = "yellow2", font = "none 15", bg = "#0068D0")
            Err.pack()
            U = Button(Sel, font = "none 10", text = "UPDATE", command = lambda: Update(E))
            U.pack()

        emp = employee.split(',')
        emp = emp[1:4]
        Label(Fr, text = "Select the attribute that needs to be changed:", bg = "#0068D0", fg = "white", font = "none 15").grid(row = 0, columnspan = 2)
        Label(Fr, text = "First Name:", bg = "#0068D0", fg = "white", font = "none 15").grid(row = 1, sticky = E)
        Label(Fr, text = "Last Name:", bg = "#0068D0", fg = "white", font = "none 15").grid(row = 2, sticky = E)
        Label(Fr, text = "Email:", bg = "#0068D0", fg = "white", font = "none 15").grid(row = 3, sticky = E)
        Button(Fr, font = "none 10", text = emp[0], width = 28, command = lambda: Select(Fr,emp[0])).grid(row = 1, column = 1)
        Button(Fr, font = "none 10", text = emp[1], width = 28, command = lambda: Select(Fr,emp[1])).grid(row = 2, column = 1)
        Button(Fr, font = "none 10", text = emp[2], width = 28, command = lambda: Select(Fr,emp[2])).grid(row = 3, column = 1)
    def get(inFile):
        z = 0
        temp = []
        v = StringVar()
        x = "Searching"
        chk = ""
        while z < 3:
            z += 1
            x = x + "."
            b.config(text = x, fg = "white", font = "none 15")
            b.update()
            time.sleep(.25)
        global g
        g = a.get()
        a.delete(0, 'end')
        g = g.lower()
        with open(inFile) as f:
            line = f.readline()
            while True:
                line = f.readline()
                if line == "":
                    if len(temp) > 1:
                        Fr.pack()
                        a.destroy()
                        for emp in temp:
                            RB = Radiobutton(Fr, variable = v, value = emp, text = emp, height = 2, overrelief = SUNKEN, indicatoron = 0, command = lambda emp=emp: Shorb(emp))
                            RB.pack()
                    if chk == False:
                        b.config(text = "Not what you're looking for? Please try agin.", fg = "yellow2", font = "none 15")
                        b.update()
                        break
                    if chk == True:
                        b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                        b.update()
                        break
                    if len(temp) == 0:
                        b.config(text = "Employee not found! Please try again.", fg = "yellow2", font = "none 15")
                        b.update()
                        break
                    if len(temp) == 1:
                        s.config(text = "Enter an attribute of the employee who's attribute needs updating:", fg = "white", font = "none 15")
                        s.update()
                        chk = Check(temp[0])
                        if chk == True:
                            Show(C, temp[0])
                        else:
                            F.pack()
                            b.config(text = "Not what you're looking for? Please try agin.", fg = "yellow2", font = "none 15")
                            b.update()
                    break
                emp = line.split(',')
                emply = [emp[0],emp[3]]
                first = emp[1]
                last = emp[2]
                name = first + " " + last
                if g in emply:
                    for atr in emply:
                        if g == atr.lower():
                            b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                            b.update()
                            F.pack_forget()
                            chk = Check(line)
                            if chk == True:
                                Show(C,line)
                            else:
                                b.config(text = "")
                                b.update()
                                F.pack()
                elif g == name.lower():
                    b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                    b.update()
                    F.pack_forget()
                    chk = Check(line)
                    if chk == True:
                        Show(C,line)
                    else:
                        b.config(text = "")
                        b.update()
                        F.pack()
                elif g == first.lower():
                    b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                    b.update()
                    temp.append(line)
                    F.pack_forget()
                    s.config(text = "Select the employee:", fg = "lime", font = "none 15")
                    s.update()
                    #List of all with that name.
                elif g == last.lower():
                    b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                    b.update()
                    temp.append(line)
                    F.pack_forget()
                    s.config(text = "Select the employee:", fg = "lime", font = "none 15")
                    s.update()
                    #List of all with that name.
    a = Entry(C, font = "none 12")
    a.pack()
    b = Label(C, bg = "#0068D0", fg = "white", font = "none 15")
    b.pack()
    c = Button(C, font = "none 10", text = "CHANGE", command = lambda: Chang(C,ge))
    F = Button(C, font = "none 10", text = "FIND", command = lambda: get(inFile))
    F.pack()
    Button(C, font = "none 10", text="MENU", width = 12, command = lambda: RTM(C)).pack(side = BOTTOM)

def Reassign(inFile):
    wind.config(menu = "")
    MenuBar.pack_forget()
    R = Frame(wind, bg = "#0068D0")
    R.pack()
    Fr = Frame(R, bg = "#0068D0")
    s = Label(R, text = "Enter an attribute of the employee who's transferring departments:", bg = "#0068D0", fg = "white", font = "none 15")
    s.pack()
    def Trans(frm,employee):
        frm.destroy()
        Tr = Frame(wind, bg = "#0068D0")
        Tr.pack()
        Fr = Frame(Tr, bg = "#0068D0")
        Fr.pack()
        Br = Frame(Tr, bg = "#0068D0")
        Br.pack(side = BOTTOM)
        emp = lst
        global oldDept
        oldDept = emp[5]
        Label(Fr, text = "Select the department the employee is being transferred to:", bg = "#0068D0", fg = "white", font = "none 15").grid(row = 0, columnspan = 2)
        Stat = Label(Fr, fg = "blue", relief = RIDGE, width = 24, bg = "white")
        Stat.grid(row = 1, columnspan = 2)
        def Sub(prev,new):
            LF = Label(Tr, bg = "#0068D0", fg = "white", font = "none 15")
            LF.pack()
            Br.destroy()
            if prev == new:
                LF.config(text = "Employee is already in this department!", fg = "yellow2", font = "none 15")
                LF.update()
            else:
                f = open(inFile)
                lines = f.readlines()
                f.close()
                with open(inFile, "w") as f1:
                    for line in lines:
                        if ntg in line:
                            line = line.replace(prev, new)
                            f1.write(line)
                            LF.config(text = "Employee has been transferred from\n" + prev + " ---> " + new + "\nsuccessfully!", fg = "lime", font = "none 15")
                            LF.update()
                        else:
                            f1.write(line)
        sub = Button(Br, font = "none 10", text = "SUBMIT", command = lambda: Sub(oldDept,newDept))
        def Select(unit):
            global newDept
            newDept = unit
            Stat.config(text = newDept)
            Stat.update()
            if not sub.winfo_ismapped():
                sub.grid(row = 5, columnspan = 3)
        Button(Tr, font = "none 10", text="MENU", width = 12, command = lambda: RTM(Tr)).pack(side = BOTTOM)
        x = 0
        y = 0
        for item in departments:
            Button(Br, font = "none 10", text = item, command = lambda item=item: Select(item)).grid(row = x, column = y, sticky = W+E)
            if x < 4:
                x += 1
            elif x == 4:
                y += 1
                x = 0
    def ShoSe(frm,employee):
        global ntg
        ntg = employee
        y = Label(bg = "#0068D0", fg = "white", font = "none 15")
        if not y.winfo_ismapped():
            global lst
            lst = employee.split(',')
            x = "ID-\t\t{}\nName-\t\t{} {}\nEmail-\t\t{}\nGender-\t\t{}\nDepartment-\t{}\nSalary-\t\t${}".format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6])
            y = Label(frm, text = x, justify = LEFT, fg = "lime", font = "none 15", bg = "#0068D0")
            y.pack()
            c.pack()
            a.destroy()
            s.destroy()
    def ShoRb(employee):
        global ntg
        ntg = employee
        Fr.destroy()
        global lst
        lst = employee.split(',')
        x = "ID-\t\t{}\nName-\t\t{} {}\nEmail-\t\t{}\nGender-\t\t{}\nDepartment-\t{}\nSalary-\t\t${}".format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6])
        y = Label(R, text = x, justify = LEFT, fg = "lime", font = "none 15", bg = "#0068D0")
        y.pack()
        c.pack()
        a.destroy()
        s.destroy()
    def get(inFile):
        z = 0
        temp = []
        v = StringVar()
        x = "Searching"
        chk = ""
        while z < 3:
            z += 1
            x = x + "."
            b.config(text = x, fg = "white", font = "none 15")
            b.update()
            time.sleep(.25)
        global g
        g = a.get()
        a.delete(0, END)
        g = g.lower()
        with open(inFile) as f:
            line = f.readline()
            while True:
                line = f.readline()
                if line == "":
                    if len(temp) > 1:
                        Fr.pack()
                        a.destroy()
                        for emp in temp:
                            RB = Radiobutton(Fr, variable = v, value = emp, text = emp, height = 2, overrelief = SUNKEN, indicatoron = 0, command = lambda emp=emp: ShoRb(emp))
                            RB.pack()
                    if chk == False:
                        b.config(text = "Not what you're looking for? Please try agin.", fg = "yellow2", font = "none 15")
                        b.update()
                        break
                    if chk == True:
                        b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                        b.update()
                        break
                    if len(temp) == 0:
                        b.config(text = "Employee not found! Please try again.", fg = "yellow2", font = "none 15")
                        b.update()
                        break
                    if len(temp) == 1:
                        s.config(text = "Enter an attribute of the employee who's transferring departments:", fg = "white", font = "none 15")
                        s.update()
                        chk = Check(temp[0])
                        if chk == True:
                            ShoSe(R, temp[0])
                            a.destroy()
                        else:
                            F.pack()
                            b.config(text = "Not what you're looking for? Please try agin.", fg = "yellow2", font = "none 15")
                            b.update()
                    break
                emp = line.split(',')
                emply = [emp[0],emp[3]]
                first = emp[1]
                last = emp[2]
                name = first + " " + last
                if g in emply:
                    for atr in emply:
                        if g == atr.lower():
                            b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                            b.update()
                            F.pack_forget()
                            chk = Check(line)
                            if chk == True:
                                ShoSe(R,line)
                                a.destroy()
                            else:
                                b.config(text = "")
                                b.update()
                                F.pack()
                elif g == name.lower():
                    b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                    b.update()
                    F.pack_forget()
                    chk = Check(line)
                    if chk == True:
                        ShoSe(R,line)
                        a.destroy()
                    else:
                        b.config(text = "")
                        b.update()
                        F.pack()
                elif g == first.lower():
                    b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                    b.update()
                    temp.append(line)
                    F.pack_forget()
                    s.config(text = "Select the employee:", fg = "lime", font = "none 15")
                    s.update()
                elif g == last.lower():
                    b.config(text = "Here's what we found.", fg = "white", font = "none 15")
                    b.update()
                    temp.append(line)
                    F.pack_forget()
                    s.config(text = "Select the employee:", fg = "lime", font = "none 15")
                    s.update()
    a = Entry(R, font = "none 12")
    a.pack()
    b = Label(R, bg = "#0068D0", fg = "white", font = "none 15")
    b.pack()
    c = Button(R, font = "none 10", text = "TRANSFER", command = lambda: Trans(R,lst))
    F = Button(R, font = "none 10", text = "FIND", command = lambda: get(inFile))
    F.pack()
    Button(R, font = "none 10", text="MENU", width = 12, command = lambda: RTM(R)).pack(side = BOTTOM)

def Report(inFile):
    wind.config(menu = "")
    MenuBar.pack_forget()
    R = Frame(wind, bg = "#0068D0")
    R.pack()
    Button(R, font = "none 10", text="MENU", width = 12, command = lambda: RTM(R)).pack(side = BOTTOM)

    fig = Figure(figsize = (7,7), dpi = 100)
    a = fig.add_subplot(111, facecolor = "k")
    fig.suptitle("Number of People by Gender", fontsize = 12)
    a.set_xlabel("Gender")
    a.set_ylabel("Amount Counted in Database")
    df = pd.read_csv(inFile, sep = ",")
    x = df.Gender.unique().tolist()
    y = pd.value_counts(df.Gender).tolist()
    a.bar(x,y, color = "c")
    canvas = FigureCanvasTkAgg(fig, R)
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)

def MenuPage(frm):
    #Instructional presentation.
    frm.destroy()
    if not MenuBar.winfo_ismapped():
        MenuBar.pack()
        Label(MenuBar, relief = RIDGE, text = "Press a button in the menu bar on the top left of your screen.\nThe following are the current features available.", font = "none 18 bold", fg = "light blue", bg = "medium blue").pack(fill = X)

        Label(MenuBar, text = """Search : Searches for an employee by entering an attribute and returns employee's information. ex: 'ID #'
              \nHire : Prompts you to enter in the information of the new employee.
              \nQuit : Prompts you for the ID # of the employee retiring/ quitting.
              \nFire : Prompts you for the ID # of the employee being fired.
              \nLay off : Prompts you for the ID # of the employee being laid off.
              \nPromote : Applies a 2% preset raise to a certain employee while keeping the max salary of $100,000 in mind.
              \nChange: Allows you to find an employee then prompts you to update their information.
              \nReassign : Allows you to transfer departments.
              \nMake Report : Generates a complete employees report.
              \nUpload: Takes you to the upload screen to attach a different file.""", justify = LEFT, anchor = "w", relief = RIDGE, bg = "#0068D0", fg = "white", font = "none 14").pack()
        DMB2.add_command(label = "Search", command = lambda: Search(inFile))
        DMB2.add_command(label = "Hire", command = lambda: Hire(inFile,outFile))
        DMB2.add_separator()
        DMB2.add_command(label = "Quit", command = lambda: Quit(inFile,outFile))
        DMB2.add_command(label = "Fire", command = lambda: Fire(inFile,outFile))
        DMB2.add_command(label = "Lay Off", command = lambda: LayOff(inFile,outFile))
        DMB2.add_separator()
        DMB2.add_command(label = "Promote", command = lambda: Promote(inFile))
        DMB2.add_command(label = "Change", command = lambda: Change(inFile))
        DMB2.add_command(label = "Reassign", command = lambda: Reassign(inFile))
        DMB2.add_separator()
        DMB2.add_command(label = "Create Report", command = lambda: Report(inFile))

        DMB.add_command(label = "Upload", command = Upload, activebackground = "green4")
        DMB.add_separator()
        DMB.add_command(label = "Exit", command = close_window, activebackground = "red")

        photo2 = PhotoImage(file = "nypa2.png")
        p2 = Label(MenuBar, image = photo2)
        p2.photo2 = photo2
        p2.pack()

        FStat.config(text = "Employee File: " + inFile + "\nArchive File: " + outFile)
        FStat.update()
        MB.add_cascade(label = "File", menu = DMB)
        MB.add_cascade(label = "Features", menu = DMB2)
        wind.config(menu = MB)

NextPage1 = Button(F3, font = "none 10", text = "NEXT", command = lambda: MenuPage(F3))
FStat = Label(MenuBar, fg = "green2", font = "none 11", bg = "navy", relief = RIDGE)
FStat.pack(fill = X)

def RTM(frm):
    frm.destroy()
    if not MenuBar.winfo_ismapped():
        MenuBar.pack()
        wind.config(menu = MB)

Button(wind, font = "none 10", text = "EXIT", width = 10, command = close_window).pack(side = BOTTOM)
wind.mainloop()
