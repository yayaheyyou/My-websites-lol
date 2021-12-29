# Modules:

import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk 
from itertools import count

# Setting things up:

Root = tk.Tk()

Root.iconbitmap("C:\\Users\\ascom\\Desktop\\Resturantimgs\\Dank_memer.ico")

Root.title("Dank-Clicker!")

Main = tk.Canvas(Root, width = 700, height = 500, relief = 'raised')
Main.pack()

MainFrame = Frame(Root)

# Declaring some variables:

# The points shown:

PTS = 0

PTSCounter = tk.Label(Root, text = PTS, fg="black")
PTSCounter.config(font=('bold', 20))
Main.create_window(100, 50, window = PTSCounter)

PTSLabel = tk.Label(Root, text = "Points:", fg="black")
PTSLabel.config(font=('bold', 20))
Main.create_window(10, 50, window = PTSLabel)

# The first upgrade button:

Upgrade10 = Button(Root, text = "Upgrade\nCost: 10")
Main.create_window(200, 70, window = Upgrade10)

# The timer:

Timer = tk.Label(Root, fg="red",)
Timer.config(font=('bold', 20))
Main.create_window(700, 20, window = Timer)

TimerLabel = tk.Label(Root, text = "Time:",  fg="black")
TimerLabel.config(font=('bold', 30))
Main.create_window(600, 20, window = TimerLabel)

# Images used:

BTN = ImageTk.PhotoImage(Image.open("C:\\Users\\ascom\\Desktop\\Resturantimgs\\Dank_memer.png"))
BTN2 = ImageTk.PhotoImage(Image.open("C:\\Users\\ascom\\Desktop\\Resturantimgs\\Dank_memer2.png"))
BTN3 = ImageTk.PhotoImage(Image.open("C:\\Users\\ascom\\Desktop\\Resturantimgs\\Dank_memer3.jpg"))
BTN4 = ImageTk.PhotoImage(Image.open("C:\\Users\\ascom\\Desktop\\Resturantimgs\\Dank_memer4.jpg"))
BTN5 = ImageTk.PhotoImage(Image.open("C:\\Users\\ascom\\Desktop\\Resturantimgs\\Dank_memer5.gif"))
BTNimg = Button(Root, image = BTN)
Main.create_window(200, 200, window=BTNimg)


# Functions:

# Seconds timer:
def start_counter(Timer):
    counter = count(0)
    def update_func():
        Timer.config(text=str(next(counter)))
        Timer.after(1000, update_func)  # 1000ms
    update_func()

# Upgrades:

def Upgrade1 (event):
    global PTS
    global Cong
    global Error
    global Upgrade100
    global MPS
    if (PTS == 10):
     PTS -= 10
     MPS = tk.Label(Root, text = "2 Points per click")
     MPS.config(font=('bold', 20))
     Main.create_window(0, 200, window = MPS)
     BTNimg.config(image = BTN2)
     PTSCounter.config(text = PTS)
     Cong = tk.Label(Root, text = "CONGRATS", fg = "black")
     Cong.config(font=('bold', 10))
     Main.create_window(200, 300, window=Cong)
     BTNimg.unbind('<Button-1>')
     BTNimg.bind('<Button-1>', IncrementBy2)
     Upgrade10.unbind('<Button-1>')
     Cong.after(3000, Cong.destroy)
     Upgrade10.after(1, Upgrade10.destroy)
     Upgrade100 = Button(Root, text = "Upgrade\nCost: 100")
     Main.create_window(200, 70, window = Upgrade100)
     Upgrade100.bind('<Button-1>', Upgrade2)
    elif (PTS >= 10) :
     PTS -= 10
     MPS = tk.Label(Root, text = "2 Points per click")
     MPS.config(font=('bold', 20))
     Main.create_window(20, 200, window = MPS)
     BTNimg.config(image = BTN2)
     PTSCounter.config(text = PTS)
     Cong = tk.Label(Root, text = "CONGRATS", fg = "black")
     Cong.config(font=('bold', 10))
     Main.create_window(200, 300, window=Cong)
     BTNimg.unbind('<Button-1>')
     BTNimg.bind('<Button-1>', IncrementBy2)
     Upgrade10.unbind('<Button-1>')
     Cong.after(3000, Cong.destroy)
     Upgrade10.after(1, Upgrade10.destroy)
     Upgrade100 = Button(Root, text = "Upgrade\nCost: 100")
     Main.create_window(200, 70, window = Upgrade100)
     Upgrade100.bind('<Button-1>', Upgrade2)
    elif (PTS <= 10):
        Error = tk.Label(Root, text = "Unsuffecient Funds!", fg = "red")
        Error.config(font=('bold', 10))
        Main.create_window(200, 400, window = Error)
        Error.after(1000, Error.destroy)

#--------------------------------------------------------------------------------

def Upgrade2 (event):
    global PTS
    global Cong
    global Error
    global Upgrade1000
    if (PTS == 100):
     PTS -= 100
     MPS.config(text = "10 Points per click")
     BTNimg.config(image = BTN3)
     PTSCounter.config(text = PTS)
     Cong = tk.Label(Root, text = "CONGRATS", fg = "black")
     Cong.config(font=('bold', 10))
     Main.create_window(200, 300, window=Cong)
     BTNimg.unbind('<Button-1>')
     BTNimg.bind('<Button-1>', IncrementBy10)
     Upgrade100.unbind('<Button-1>')
     Cong.after(3000, Cong.destroy)
     Upgrade100.after(1, Upgrade100.destroy)
     Upgrade1000 = Button(Root, text = "Upgrade\nCost: 1,000")
     Main.create_window(200, 70, window = Upgrade1000)
     Upgrade1000.bind('<Button-1>', Upgrade3)
    elif (PTS >= 100) :
     PTS -= 100
     MPS.config(text = "10 Points per click")
     BTNimg.config(image = BTN3)
     PTSCounter.config(text = PTS)
     Cong = tk.Label(Root, text = "CONGRATS", fg = "black")
     Cong.config(font=('bold', 10))
     Main.create_window(200, 300, window=Cong)
     BTNimg.unbind('<Button-1>')
     BTNimg.bind('<Button-1>', IncrementBy10)
     Upgrade100.unbind('<Button-1>')
     Cong.after(3000, Cong.destroy)
     Upgrade100.after(1, Upgrade100.destroy)
     Upgrade1000 = Button(Root, text = "Upgrade\nCost: 1,000")
     Main.create_window(200, 70, window = Upgrade1000)
     Upgrade1000.bind('<Button-1>', Upgrade3)
    elif (PTS <= 100):
        Error = tk.Label(Root, text = "Unsuffecient Funds!", fg = "red")
        Error.config(font=('bold', 10))
        Main.create_window(200, 400, window = Error)
        Error.after(1000, Error.destroy)


#--------------------------------------------------------------------------------

def Upgrade3 (event):
    global PTS
    global Cong
    global Error
    global Upgrade10000
    global Upgrade1000
    if (PTS == 1000):
     PTS -= 1000
     MPS.config(text = "100 Points per click")
     BTNimg.config(image = BTN4)
     PTSCounter.config(text = PTS)
     Cong = tk.Label(Root, text = "CONGRATS", fg = "black")
     Cong.config(font=('bold', 10))
     Main.create_window(200, 300, window=Cong)
     BTNimg.unbind('<Button-1>')
     BTNimg.bind('<Button-1>', IncrementBy100)
     Upgrade1000.unbind('<Button-1>')
     Upgrade10000 = Button(Root, text = "Upgrade\nCost:10,000")
     Main.create_window(200, 70, window = Upgrade10000)
     Upgrade10000.bind('<Button-1>', Upgrade4)

    elif (PTS >= 1000) :
     PTS -= 1000
     MPS.config(text = "100 Points per click")
     BTNimg.config(image = BTN4)
     PTSCounter.config(text = PTS)
     Cong = tk.Label(Root, text = "CONGRATS", fg = "black")
     Cong.config(font=('bold', 10))
     Main.create_window(200, 300, window=Cong)
     BTNimg.unbind('<Button-1>')
     BTNimg.bind('<Button-1>', IncrementBy100)
     Upgrade1000.unbind('<Button-1>')
     Cong.after(3000, Cong.destroy)
     Upgrade100.after(1, Upgrade1000.destroy)
     Upgrade10000 = Button(Root, text = "Upgrade\nCost: 10,000")
     Main.create_window(200, 70, window = Upgrade10000)
     Upgrade10000.bind('<Button-1>', Upgrade4)
    
    elif (PTS <= 1000):
        Error = tk.Label(Root, text = "Unsuffecient Funds!", fg = "red")
        Error.config(font=('bold', 10))
        Main.create_window(200, 400, window = Error)
        Error.after(1000, Error.destroy)

#--------------------------------------------------------------------------------

def Upgrade4(event):
    global PTS
    global Cong
    global Error
    global Upgrade10000
    global Upgrade1000
    global Upgrade50000
    global PetsMenu
    global PetCounter
    global Foxes
    if (PTS == 10000):
     PTS -= 10000
     MPS.config(text = "1000 Points per click")
     BTNimg.config(image = BTN5)
     PTSCounter.config(text = PTS)
     Cong = tk.Label(Root, text = "CONGRATS\nYou are now able to buy pets in the pets list.", fg = "black")
     Cong.config(font=('bold', 10))
     Main.create_window(200, 300, window=Cong)
     BTNimg.unbind('<Button-1>')
     BTNimg.bind('<Button-1>', IncrementBy1000)
     Upgrade10000.unbind('<Button-1>')
     Upgrade10000.after(1, Upgrade10000.destroy)
     Upgrade50000 = tk.Label(Root, text = "Upgrade\nCost: 50,000")
     Main.create_window(200, 70, window = Upgrade50000)
     PetsMenu = Button(Root, text = "Pets Menu")
     Main.create_window(500, 200, window = PetsMenu)
     PetsMenu.bind('<Button-1>', PetsWindow)
     Foxes = 0
     PetCounter = tk.Label(Root, text = "You have:\nFoxes: " + str(Foxes) + ".")
     Main.create_window(200, 250, window = PetCounter)
    elif (PTS >= 10000) :
     PTS -= 10000
     MPS.config(text = "1000 Points per click")
     BTNimg.config(image = BTN5)
     PTSCounter.config(text = PTS)
     Cong = tk.Label(Root, text = "CONGRATS\nYou are now able to buy pets in the pets list.", fg = "black")
     Cong.config(font=('bold', 10))
     Main.create_window(200, 300, window=Cong)
     BTNimg.unbind('<Button-1>')
     BTNimg.bind('<Button-1>', IncrementBy1000)
     Upgrade10000.unbind('<Button-1>')
     Cong.after(3000, Cong.destroy)
     Upgrade10000.after(1, Upgrade10000.destroy)
     Upgrade50000 = Button(Root, text = "Upgrade\nCost: 50,000")
     Main.create_window(200, 70, window = Upgrade50000)
     PetsMenu = Button(Root, text = "Pets Menu")
     Main.create_window(500, 200, window = PetsMenu)
     PetsMenu.bind('<Button-1>', PetsWindow)
     Foxes = 0
     PetCounter = tk.Label(Root, text = "You have:\nFoxes: " + str(Foxes) + ".")
     Main.create_window(200, 250, window = PetCounter)
     
    elif (PTS <= 10000):
        Error = tk.Label(Root, text = "Unsuffecient Funds!", fg = "red")
        Error.config(font=('bold', 10))
        Main.create_window(200, 400, window = Error)
        Error.after(1000, Error.destroy)

def PetsWindow (event):
    global BuyFox
    global Foxes
    global Main2
    newWindow = Toplevel()
    newWindow.title("Pets")
    newWindow.geometry("200x200")
    Main2 = tk.Canvas(newWindow, width = 200, height = 200, relief='raised')
    Main2.pack()
    Foxes = 0
    BuyFoxBtn = Button(newWindow, text = "Buy a pet fox\nCost: 1000\nAbilities: X2 Points per click.")
    Main2.create_window(100 , 30 , window = BuyFoxBtn)
    BuyFoxBtn.bind('<Button-1>', BuyFox)
    

# Functions for incrementing:

def IncreasePTS (event):
    global PTS
    PTS += 1
    PTSCounter.config(text = PTS)

def IncrementBy2 (event):
    global PTS
    PTS += 2
    PTSCounter.config(text = PTS)

def IncrementBy10 (event):
    global PTS
    PTS += 10
    PTSCounter.config(text = PTS)

def IncrementBy100 (event):
    global PTS
    PTS += 100
    PTSCounter.config(text = PTS)

def IncrementBy1000(event):
    global PTS
    PTS += 1000
    PTSCounter.config(text = PTS)

# Admin button:

def Admin (event):
    global PTS
    PTS += 10000
    PTSCounter.config(text = PTS)

# Pets:

def BuyFox (event):
    global Foxes
    global PTS
    Foxes += 1
    PTS -= 1000
    PetCounter.config(text = f"You have:\nFoxes: {Foxes}")





 
# Using functions:



start_counter(Timer)

# Binding:

BTNimg.bind('<Button-1>', IncreasePTS)
Upgrade10.bind('<Button-1>', Upgrade1)
admin = Button(Root, text = "E")
Main.create_window(700, 500, window = admin)
admin.bind('<Button-1>', Admin)


Root.mainloop()


