import tkinter
from tkinter import messagebox

top = tkinter.Tk()

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(text ="Hello", command = helloCallBack, activebackground = "Red", activeforeground = "Yellow",bg = "Purple", font = "Monospace")
A = tkinter.Button(text = "Hi!", highlightcolor = "Violet")
A.place(x = 60, y = 150)
B.place(x = 1, y = 150)
B.pack()
top.geometry("600x600")
top.mainloop()

