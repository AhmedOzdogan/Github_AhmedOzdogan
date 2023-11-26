# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 23:13:05 2020

@author: Ahmed
"""

from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Calculator")
root.geometry("320x530")

"""Functions"""
    
def button_1(x):
    write(x)
    
def close():
    answer = tkinter.messagebox.askquestion("Attention", "Do you really want to close program")
    
    if answer == "yes":
        root.destroy()
        

def write(x):
    s = len(cal.get())
    cal.insert(s, str(x))
    
operation = 5  
n1 = 0
    
def calculate(y):
    global operation
    global n1
    operation = y
    n1 = float(cal.get())
    cal.delete(0,"end")
    
n2 = 0,

def result():
    global n2
    n2 = float(cal.get())
    global operation
    cal.delete(0,"end")
    res = 0
    if operation == 1:
        res = n1/n2
    elif operation == 2:
        res = n1*n2
    elif operation == 3:
        res = n1-n2
    elif operation == 4:
        res = n1+n2
    
    if res % 10 == 0 :
        res = int(res)
    
    cal.insert(0,str(res))
    
def del1():
    global operation
    global n1
    global n2
    cal.delete(0,'end')
    n2 = 0
    n1 = 0
    operation = 5

def del2():
    cal.delete(0,'end')
    
def del3():
    l_line = len(cal.get())-1
    cal.delete(l_line)
        
    

def minus():
    m_1 = cal.get()
    if m_1[:1] != "-":
        cal.insert(0, "-")
    else:
        cal.delete(0)

"""Creating Menu"""

menu_ = Menu(root)
root.config(menu = menu_)

menu_sub = Menu(menu_, tearoff = 0)
menu_.add_cascade(label = "File", menu=menu_sub)

menu_sub.add_command(label = "Exit", command = close)

"""Frames"""

frame_1 = Frame(root)
frame_1.pack()


"""Buttons"""

h = 5
w = 10

"""NUmbers"""

b = [] #for kullanma !!!!!!

button_7 = Button(frame_1, text = "7", height = h,
                  width = w,
                  command = lambda x = 8 : write(x))
button_7.grid(row = 2, column = 0)

button_8 = Button(frame_1, text = "8",height = h,
                  width = w,
                  command = lambda x = 8 : write(x))
button_8.grid(row = 2, column = 1)

button_9 = Button(frame_1, text = "9",height = h,
                  width = w,
                  command = lambda x = 9 : write(x))

button_9.grid(row = 2, column = 2)

button_4 = Button(frame_1, text = "4",height = h,
                  width = w,
                  command = lambda x = 4 : write(x))

button_4.grid(row = 3, column = 0)

button_5 = Button(frame_1, text = "5",height = h,
                  width = w,
                  command = lambda x = 5 : write(x))

button_5.grid(row = 3, column = 1)

button_6 = Button(frame_1, text = "6",height = h,
                  width = w,
                  command = lambda x = 6 : write(x))

button_6.grid(row = 3, column = 2)

button_1 = Button(frame_1, text = "1",height = h,
                  width = w,
                  command = lambda x = 1 : write(x))

button_1.grid(row = 4, column = 0)

button_2 = Button(frame_1, text = "2",height = h,
                  width = w,
                  command = lambda x = 2 : write(x))

button_2.grid(row = 4, column = 1)

button_3 = Button(frame_1, text = "3",height = h,
                  width = w,
                  command = lambda x = 3 : write(x))

button_3.grid(row = 4, column = 2)

button_10 = Button(frame_1, text = "+/-",height = h,
                  width = w,
                  command = minus)

button_10.grid(row = 5, column = 0)

button_0 = Button(frame_1, text = "0",height = h,
                  width = w,
                  command = lambda x = 0 : write(x))

button_0.grid(row = 5, column = 1)

button_11 = Button(frame_1, text = ".",height = h,
                  width = w,
                  command = lambda x = "." : write(x))

button_11.grid(row = 5, column = 2)

""" Signs"""

h_1 = int(h*4/5)
button_12 = Button(frame_1, text = "/", height = h,
                  width = w,
                  command = lambda y = 1 : calculate(y))

button_12.grid(row = 2, column = 3)

button_13 = Button(frame_1, text = "*",height = h,
                  width = w,
                  command = lambda y = 2 : calculate(y))

button_13.grid(row = 3, column = 3)

button_14 = Button(frame_1, text = "-",height = h,
                  width = w,
                  command = lambda y = 3 : calculate(y))

button_14.grid(row = 4, column = 3)

button_15 = Button(frame_1, text = "+",height = h,
                  width = w,
                  command = lambda y = 4 : calculate(y))

button_15.grid(row = 5, column = 3)

button_16 = Button(frame_1, text = "=",height = h,
                  width = w,
                  command = result)
button_16.grid(row = 6, column = 0)

button_16 = Button(frame_1, text = "C",height = h,
                  width = w,
                  command = del1)
button_16.grid(row = 6, column = 1)

button_17 = Button(frame_1, text = "CE",height = h,
                  width = w,
                  command = del2)
button_17.grid(row = 6, column = 2)

button_18 = Button(frame_1, text = "<=",height = h,
                  width = w,
                  command = del3)

button_18.grid(row = 6, column = 3)

"""Entry"""

cal = Entry(frame_1,justify = RIGHT,
                  width = 14, font = "Ariel 29 bold")
cal.grid(row = 0, column = 0, columnspan = 4)

cal_1 = Entry(frame_1,justify = RIGHT,
                  width = 14, font = "Ariel 29 bold")
cal_1.grid(row = 1, column = 0, columnspan = 4)



root.mainloop()