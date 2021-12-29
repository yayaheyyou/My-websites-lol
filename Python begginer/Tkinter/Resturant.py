# Modules:

import tkinter
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from tkinter import Tk,ttk,Tcl 
import tkinter as tk
import os

# Setting things up:

Root = tk.Tk()

Main_Frame = Frame(Root)

Canvas1 = tk.Canvas(Root, width = 700, height = 1000, relief='raised')
Canvas1.pack()

Money = 1000

MoneyLabel = tk.Label(Root, text = Money)
MoneyLabel.config(font =('bold', 15))
Canvas1.create_window(200, 25, window=MoneyLabel)


global Remainder2Label
global fade_away
Bananas = 0

# Functions:

def Error (event):
    global fade_away
    global ErrorLabel
    ErrorLabel = tk.Label(Root, text = "You can't buy more than the quantity of 3 of a certain item!", bg = "Blue")
    ErrorLabel.config(font =('bold', 15))
    Canvas1.create_window(250, 25, window=ErrorLabel)
    ErrorLabel.after(1000, ErrorLabel.destroy)
    


def buyBanana (event):
    global Remainder 
    global RemainderLabel
    global BananasRem
    BananasRem = Bananas + 1
    BananasRemDis = tk.Label(Root, text = BananasRem)
    BananasRemDis.config(font=('bold', 25))
    Canvas1.create_window(200, 300, window=BananasRemDis)
    MoneyLabel.destroy() 
    Remainder = Money - 100
    RemainderLabel = tk.Label(Root, text = Remainder)
    RemainderLabel.config(font =('bold', 15))
    Canvas1.create_window(200, 25, window=RemainderLabel)
    Bananaimg.bind('<Double-1>', buy2Bananas)
    
    
def buy2Bananas (event):
         global Remainder2
         global BananasRem2
         if Remainder > 100:
          RemainderLabel.destroy() 
          MoneyLabel.destroy()
          Remainder2 = Remainder - 100
          Remainder2Label = tk.Label(Root, text = Remainder2)
          Remainder2Label.config(font =('bold', 15))
          Canvas1.create_window(200, 25, window=Remainder2Label)
          Bananaimg.unbind('<Double-1>') 
          Bananaimg.bind('<Triple-1>',  buy3Bananas)
          BananasRem2 = BananasRem + 1
          BananasRem2Dis = tk.Label(Root, text = BananasRem2)
          BananasRem2Dis.config(font=('bold', 25))
          Canvas1.create_window(200, 300, window=BananasRem2Dis)


def buy3Bananas (event):
         Remainder2Label = tk.Label(Root, text = Remainder2)
         if Remainder > 100:
          Remainder2Label.destroy()
          MoneyLabel.destroy()
          Remainder3 = Remainder2 - 100
          Remainder3Label = tk.Label(Root, text = Remainder3)
          Remainder3Label.config(font =('bold', 15))
          Canvas1.create_window(200, 25, window=Remainder3Label)
          Bananaimg.unbind('<Triple-1>')
          Bananaimg.bind('<Quadruple-1>', Error)
          BananasRem3 = BananasRem2 + 1
          BananasRem3Dis = tk.Label(Root, text = BananasRem3)
          BananasRem3Dis.config(font=('bold', 25))
          Canvas1.create_window(200, 300, window=BananasRem3Dis)
          
          
          

         





    
# Starting:

Banana = ImageTk.PhotoImage(Image.open("C:\\Users\\ascom\\Desktop\\Resturantimgs\\Banana2.png"))
Bananaimg = Button(Root, image = Banana)
Canvas1.create_window(200, 200, window=Bananaimg)
Bananaimg.bind('<Button-1>', buyBanana)
BananasDis = tk.Label(Root, text = Bananas)
BananasDis.config(font=('bold', 25))
Canvas1.create_window(200, 300, window=BananasDis)


Root.mainloop()