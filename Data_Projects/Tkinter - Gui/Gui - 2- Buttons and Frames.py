# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 01:06:03 2020

@author: Ahmed
"""


from tkinter import *

root = Tk() 
root.geometry("300x500")


topFrame = Frame(root) #iki görünmez frame böldük. invisible containers

topFrame.pack()

bottomFrame = Frame(root)

bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "Click - Button 1", fg="red") 

button2 = Button(topFrame, text = "Click - Button 2", fg="blue") 

button3 = Button(topFrame, text = "Click - Button 3", fg="green") 

button4 = Button(bottomFrame, text = "Click - Button 4", fg="black") 

button1.pack(side = LEFT) #as far left as possible
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = RIGHT)


root.mainloop()