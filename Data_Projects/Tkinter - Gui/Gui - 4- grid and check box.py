# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 01:26:26 2020

@author: Ahmed
"""

from tkinter import *

root = Tk() 

label_1 = Label(root, text = "Name")

label_2 = Label(root, text = "Password")

entry_1 = Entry(root)

entry_2 = Entry(root)

label_1.grid(row = 0, column = 0, sticky=E) #grid is used for organised labels. if we dont write column it will assume 0
label_2.grid(row = 1, sticky=E)  #E means put it on East. East, west, south, norht.

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)

c = Checkbutton(root, text = "Keep me logged in")

c.grid(columnspan = 2) # use two column



















root.mainloop()
