# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 01:20:30 2020

@author: Ahmed
"""

from tkinter import *

root = Tk() 

one = Label(root, text = "One", bg = "red", fg = "Blue") #bg is geri plan foreground, fg is text colour 

one.pack()

two = Label(root, text = "two", bg = "Black", fg = "White")
            
two.pack(fill = X) # fill=x fill it as long as it isi possible. black will be in everywhere

three = Label(root, text = "twp", bg = "Green", fg = "White")

three.pack(side = LEFT, fill = Y)



















root.mainloop()
