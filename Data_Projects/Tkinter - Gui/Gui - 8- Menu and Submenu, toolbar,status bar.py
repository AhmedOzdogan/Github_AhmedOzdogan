# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 00:50:47 2020

@author: Ahmed
"""

from tkinter import *


def doNothing():
    print("ok ok ok I won't")

root = Tk() 

root.title("Ahmed")

width  = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{500}x{500}')



menu_atTop = Menu(root)
root.config(menu=menu_atTop) #always it puts it to the top


sub_menu_atTop = Menu(menu_atTop, tearoff=0) #created a submenu, close the dashes.
menu_atTop.add_cascade(label="File", menu=sub_menu_atTop)
sub_menu_atTop.add_command(label="New Project...", command=doNothing) #submenu items.
sub_menu_atTop.add_command(label="New Project 2", command=doNothing)
sub_menu_atTop.add_separator()
sub_menu_atTop.add_command(label="Exit", command=root.destroy)

edit_menu_atTop = Menu(menu_atTop, tearoff=0)
menu_atTop.add_cascade(label="Edit", menu=edit_menu_atTop)
edit_menu_atTop.add_command(label="Undo", command=doNothing)



"""Toolbar Creator"""

toolbar = Frame(root, bg="blue")

insertButton = Button(toolbar, text="insert a image", command=doNothing)
insertButton.pack(side = LEFT, padx=2, pady=2)
printButton = Button(toolbar, text="Print", command=doNothing)
printButton.pack(side = LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


"""Status Bar At Bottom"""


status = Label(root, text = "Preparing to do Nothing...", bd = 1,relief = SUNKEN, anchor = W) #bd for border at outside
status.pack(side=BOTTOM, fill = X)

























root.mainloop()

