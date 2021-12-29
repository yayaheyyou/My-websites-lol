# Modules:
import tkinter as tk
from tkinter import *
# Setting things up:

root= tk.Tk()


canvas1 = tk.Canvas(root, width = 400, height = 1000,  relief = 'raised')
canvas1.pack()

# Starting:

label1 = tk.Label(root, text='Weight calculator')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

# Pound to kilogram:

label2 = tk.Label(root, text='Pound to kilogram:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)


def getPounds ():
    
    x1 = entry1.get()
    
    res = float(x1) / 2.205


    label3 = tk.Label(root, text= x1 + ' pound(s) are: ',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    
    label4 = tk.Label(root, text= str(res) + " kg",font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Convert', command=getPounds, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)


# Stone to kilogram: 

entry2 = tk.Entry (root) 
canvas1.create_window(400, 140, window=entry2)


label5 = tk.Label(root, text='Stone to kilogram:')
label5.config(font=('helvetica', 10))
canvas1.create_window(400, 100, window=label5)

def getStone ():
    
    x2 = entry2.get()
    
    res2 = float(x2) * 6.35


    label6 = tk.Label(root, text= x2 + ' stone(s) are: ',font=('helvetica', 10))
    canvas1.create_window(400, 210, window=label6)
    
    label7 = tk.Label(root, text= str(res2) + " kilograms",font=('helvetica', 10, 'bold'))
    canvas1.create_window(400, 230, window=label7)
    
button2 = tk.Button(text='Convert', command=getStone, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(400, 180, window=button2)

# Ton to kilogram: 

entry4 = tk.Entry (root) 
canvas1.create_window(0, 140, window=entry4)


label6 = tk.Label(root, text='Ton to kilogram:')
label6.config(font=('helvetica', 10))
canvas1.create_window(0, 100, window=label6)

def getTon ():
    
    x4 = entry4.get()
    
    res = float(x4) * 907


    label6 = tk.Label(root, text= x4 + ' ton(s) are: ',font=('helvetica', 10))
    canvas1.create_window(0, 210, window=label6)
    
    label7 = tk.Label(root, text= str(res) + " kilograms",font=('helvetica', 10, 'bold'))
    canvas1.create_window(0, 230, window=label7)
    
button4 = tk.Button(text='Convert', command=getTon, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(0, 180, window=button4)

# Money calculator:

moneyTitle = tk.Label(root, text='Money calculator')
moneyTitle.config(font=('helvetica', 14))
canvas1.create_window(200, 280, window=moneyTitle)

# USD to EGP:

entry3 = tk.Entry (root) 
canvas1.create_window(200, 390, window=entry3)


label8 = tk.Label(root, text='USD to EGP:')
label8.config(font=('helvetica', 10))
canvas1.create_window(200, 350, window=label8)

def getUSD ():
    
    x3 = entry3.get()
    
    res3 = float(x3) * 15.74


    label9 = tk.Label(root, text= x3 + ' USD is: ',font=('helvetica', 10))
    canvas1.create_window(200, 460, window=label9)
    
    label7 = tk.Label(root, text= str(res3) + " EGP",font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 480, window=label7)
    
button3 = tk.Button(text='Convert', command=getUSD, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 430, window=button3)

# EUR to EGP:

entry5 = tk.Entry (root) 
canvas1.create_window(400, 390, window=entry5)


label11 = tk.Label(root, text='EUR to EGP:')
label11.config(font=('helvetica', 10))
canvas1.create_window(400, 350, window=label11)

def getEUR ():
    
    x3 = entry5.get()
    
    res3 = float(x3) * 17.69


    label9 = tk.Label(root, text= x3 + ' EUR is: ',font=('helvetica', 10))
    canvas1.create_window(400, 460, window=label9)
    
    label7 = tk.Label(root, text= str(res3) + " EGP",font=('helvetica', 10, 'bold'))
    canvas1.create_window(400, 480, window=label7)
    
button5 = tk.Button(text='Convert', command=getEUR, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(400, 430, window=button5)

# YEN to EGP:

entry6 = tk.Entry (root) 
canvas1.create_window(00, 390, window=entry6)


label12 = tk.Label(root, text='YEN to EGP:')
label2.config(font=('helvetica', 10))
canvas1.create_window(00, 350, window=label12)

def getYEN ():
    
    x3 = entry6.get()
    
    res3 = float(x3) * 0.14


    label9 = tk.Label(root, text= x3 + ' YEN is: ',font=('helvetica', 10))
    canvas1.create_window(00, 460, window=label9)
    
    label7 = tk.Label(root, text= str(res3) + " EGP",font=('helvetica', 10, 'bold'))
    canvas1.create_window(00, 480, window=label7)
    
button6 = tk.Button(text='Convert', command=getYEN, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(00, 430, window=button6)

# Length calculator:

lengthTitle = tk.Label(root, text='Length calculator')
lengthTitle.config(font=('helvetica', 14))
canvas1.create_window(200, 555, window=lengthTitle)

# Feet to CM:

entry7 = tk.Entry (root) 
canvas1.create_window(200, 670, window=entry7)


label8 = tk.Label(root, text='Feet to CMS:')
label8.config(font=('helvetica', 10))
canvas1.create_window(200, 630, window=label8)

def getFeet ():
    
    x3 = entry7.get()
    
    res3 = float(x3) * 15.74


    label9 = tk.Label(root, text= x3 + ' Feet are: ',font=('helvetica', 10))
    canvas1.create_window(200, 460, window=label9)
    
    label7 = tk.Label(root, text= str(res3) + " CMS",font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 480, window=label7)
    
button7 = tk.Button(text='Convert', command=getFeet, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 710, window=button7)

# EUR to EGP:

entry5 = tk.Entry (root) 
canvas1.create_window(400, 390, window=entry5)


label11 = tk.Label(root, text='EUR to EGP:')
label11.config(font=('helvetica', 10))
canvas1.create_window(400, 350, window=label11)

def getEUR ():
    
    x3 = entry5.get()
    
    res3 = float(x3) * 17.69


    label9 = tk.Label(root, text= x3 + ' EUR is: ',font=('helvetica', 10))
    canvas1.create_window(400, 460, window=label9)
    
    label7 = tk.Label(root, text= str(res3) + " EGP",font=('helvetica', 10, 'bold'))
    canvas1.create_window(400, 480, window=label7)
    
button5 = tk.Button(text='Convert', command=getEUR, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(400, 430, window=button5)

# YEN to EGP:

entry6 = tk.Entry (root) 
canvas1.create_window(00, 390, window=entry6)


label12 = tk.Label(root, text='YEN to EGP:')
label2.config(font=('helvetica', 10))
canvas1.create_window(00, 350, window=label12)

def getYEN ():
    
    x3 = entry6.get()
    
    res3 = float(x3) * 0.14


    label9 = tk.Label(root, text= x3 + ' YEN is: ',font=('helvetica', 10))
    canvas1.create_window(00, 460, window=label9)
    
    label7 = tk.Label(root, text= str(res3) + " EGP",font=('helvetica', 10, 'bold'))
    canvas1.create_window(00, 480, window=label7)
    
button6 = tk.Button(text='Convert', command=getYEN, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(00, 430, window=button6)



root.mainloop()
