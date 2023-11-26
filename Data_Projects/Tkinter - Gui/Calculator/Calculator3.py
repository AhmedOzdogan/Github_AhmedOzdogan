# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 21:50:35 2020

@author: Ahmed
"""


"""Bug ara,
değişiklik yapılacak,
görüntü ve boyut
"""


from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Calculator")
root.geometry("320x530")

"""FUNCTIONS """
    
def button_1(x):
    write(x)
    
def close():
    answer = tkinter.messagebox.askquestion("Attention", "Do you really want to close program")
    
    if answer == "yes":
        root.destroy()
        

def write(x):
    s = len(cal.get())
    s_1 = len(cal_2.get())
    cal.insert(s, str(x))
    cal_2.insert(s_1, str(x))
    
    global click
    click +=1
    
    
operation = 5  
n1 = 0
    
def calculate(y):
    global operation
    global n1
    operation = y
    n1 = float(cal.get())
    cal.delete(0,"end")
    
    if operation == 3:
        res_1 = "/"
       
        
    elif operation == 2:
        res_1 = "*"
        
        
    elif operation == 1:
        res_1 = "-"
        
        
    elif operation == 0:
        res_1 = "+"
    
        
    cal_2.insert(len(cal_2.get()),res_1)
    
    global click
    click = 0
    
    
n2 = 0,

def result():
    global n2
    n2 = float(cal.get())
    global operation
    cal.delete(0,"end")
    res = 0
    if operation == 3:
        res = n1/n2
       
        
    elif operation == 2:
        res = n1*n2
        
        
    elif operation == 1:
        res = n1-n2
        
        
    elif operation == 0:
        res = n1+n2
       
    
    if res - int(res) == 0:
        res = int(res)
    
    res_2 = "=" + str(res)
    print(res_2)
        
    cal.insert(0,str(res))
    
    cal_2.insert(len(cal_2.get()),res_2)
    
def del1():
    global operation
    global n1
    global n2
    cal.delete(0,'end')
    cal_2.delete(0,'end')
    n2 = 0
    n1 = 0
    operation = 5

def del2():
    cal.delete(0,'end')

click = 0
click_1 = 0

def del3():
    l_line = len(cal.get())-1
    l_line_2 = len(cal_2.get())-1
    cal.delete(l_line)
    
    global click
    global click_1
    
    if click_1<click:
        cal_2.delete(l_line_2)
        click_1 +=1
    else:
        click_1 +=1
        pass

def point(x):
    p_1 = cal.get()
    if "." in p_1 :
        pass
    else:
        cal.insert(len(cal.get()), ".")
        cal_2.insert(len(cal_2.get()), ".")
    

def minus():
    m_1 = cal.get()
    if m_1[:1] != "-":
        cal.insert(0, "-")
        cal_2.insert(0, "-")
    else:
        cal.delete(0)
        cal_2.delete(0)

        
        

h = 3

w = 5

font_1 = "Ariel 14 bold"

"""ENTRIES"""

font_2 = "Ariel 29 bold"
w_e = 10

cal = Entry(root,justify = RIGHT,
                  width = w_e, font = font_2)
cal.grid(row = 1, column = 0, columnspan = 4)

cal_2 = Entry(root,justify = RIGHT,
                  width = w_e, font = font_2)
cal_2.grid(row = 0, column = 0, columnspan = 4)

"""NUMBERS"""

buttons = []

for j in range(1,10):
    buttons.append(Button(text=str(j),font=font_1,
                          height = h, width = w,
                          command = lambda x = j : write(x)))

n = 0

for k in reversed(range(2,5)):
    for l in range(3):
        buttons[n].grid(row = k, column = l )
        n += 1
         
"""SIGNS"""

signs = []

for j in range (4):
    signs.append(Button(font=font_1,
                          height = h, width = w,
                          command = lambda y = j : calculate(y)))

signs[0]['text'] = '+'
signs[1]['text'] = '-'
signs[2]['text'] = '*'
signs[3]['text'] = '/'



for j in range (4):
    signs[j].grid(row = j+2, column = 3 )

    
button_1 = Button(root, text = "C",font=font_1,
                  height = h,
                  width = w,
                  command = del1)
button_1.grid(row = 6, column = 1)

button_2 = Button(root, text = "CE",font=font_1,
                  height = h,
                  width = w,
                  command = del2)
button_2.grid(row = 6, column = 2)

button_3 = Button(root, text = "<=",font=font_1,
                  height = h,
                  width = w,
                  command = del3)

button_3.grid(row = 6, column = 3)

button_4 = Button(root, text = "+/-",font=font_1,
                  height = h,
                  width = w,
                  command = minus)

button_4.grid(row = 5, column = 0)

button_5 = Button(root, text = "0",font=font_1,
                  height = h,
                  width = w,
                  command = lambda x = 0 : write(x))

button_5.grid(row = 5, column = 1)

button_6 = Button(root, text = ".",font=font_1,
                  height = h,
                  width = w,
                  command = lambda x = "." : point(x))

button_6.grid(row = 5, column = 2)

button_7 = Button(root, text = "=",font=font_1,
                  height = h,
                  width = w,
                  command = result)

button_7.grid(row = 6, column = 0)

root.mainloop()
