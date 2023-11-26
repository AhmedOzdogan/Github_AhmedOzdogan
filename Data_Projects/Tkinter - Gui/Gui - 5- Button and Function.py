# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 23:58:29 2020

@author: Ahmed
"""


from tkinter import *

root = Tk() 


def printName():
    print("Hello World")
    
button_1 = Button(root, text = "Print my name:)", command = printName) #fonksiyonu yazdığımızda sonunda parantez olmayacak
#binding a budget on a button


button_1.pack()

def printName_1(event):
    print("Hello World - 222222")
    
button_2 = Button(root, text = "Print my name - 2222:)") 


button_2.bind("<Button-1>", printName_1)
button_2.pack()

#yada event yazdık ve aşağıda bind komutunu kullnarak onu atadık. Button-1 sol tık demektir. 












root.mainloop()
