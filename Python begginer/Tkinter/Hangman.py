# Modules:

import tkinter as tk 
from tkinter import Canvas
from tkinter import Tk, ttk 
import random
from random_word import RandomWords


# Setting things up:

Root = tk.Tk()

# Creating the main canvas:

Main = tk.Canvas(Root, width = 400, height = 1000, relief = 'raised')
Main.pack()

# Starting:

# Declaring some useful variables:

RANDOM = RandomWords()

Word = tk.Label(Root, text=RANDOM.get_random_word())
Word.config(font =('bold', 50))
Main.create_window(200, 25, window=Word)

Main.mainloop()



