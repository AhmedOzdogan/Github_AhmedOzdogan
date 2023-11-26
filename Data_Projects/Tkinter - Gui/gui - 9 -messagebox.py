# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 04:15:04 2020

@author: Ahmed
"""


from tkinter import *

import tkinter.messagebox

root = Tk() 

tkinter.messagebox.showinfo("Window Title", "Monkeys can live up to 300 years")

answer = tkinter.messagebox.askquestion("Question 1", "Believe it?")

if answer =="yes":
    print(":/")


















































root.mainloop()