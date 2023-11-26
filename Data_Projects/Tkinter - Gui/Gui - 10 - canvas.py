# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:40:24 2020

@author: Ahmed
"""

from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackline = canvas.create_line(0, 0, 200, 50) #(x,y,x,y)

redline = canvas.create_line(0,100,200,50, fill="red")

greenbox = canvas.create_rectangle(25,25,130,60, fill="green")

# canvas.delete(redline) #deletes whatever we want within it.

# canvas.delete(ALL) #deletes all
































root.mainloop()