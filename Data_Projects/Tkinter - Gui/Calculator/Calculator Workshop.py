# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 23:11:29 2020

@author: Ahmed
"""

from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("Calculator")
# root.geometry("300x500")
root.configure(bg="gray64")

"""Menu Created"""
menu_at_top = Menu(root)
root.config(menu=menu_at_top)

"""SubMenu Created"""
sub_Menu = Menu(menu_at_top, tearoff = 0)
menu_at_top.add_cascade(label = "File", menu=sub_Menu)

"""SubMenu Items"""
sub_Menu.add_command(label = "New Calculator")
sub_Menu.add_command(label = "Exit", command = root.destroy)


"""Frames"""
# # Frame_0 = Frame(root)
# Frame_0.pack()

Frame_1 = Canvas(root)
Frame_1.pack(side = LEFT)

Frame_2 = Canvas(root)
Frame_2.pack(side = RIGHT)

# Frame_3 = Frame(root)
# Frame_3.pack(side = BOTTOM)

# Frame_4 = Frame(root)
# Frame_4.pack(side = BOTTOM)


"""Buttons"""

myFont = Font(family="Times New Roman", size=35,)
padx_number = 7

Button_7 = Button(Frame_1, text = " 7 " , fg = "gray55", height = 2, 
          width = 2) 
Button_7.configure(font=myFont, fg = "black")
Button_7.grid(row = 0, column = 0,padx = padx_number)

Button_9 = Button(Frame_1, text = " 8 " , fg = "gray55", height = 2, 
          width = 2)  
Button_9.configure(font=myFont, fg = "black")
Button_9.grid(row = 1, column = 0,padx = padx_number)

Button_8 = Button(Frame_2, text = " 9 " , fg = "gray55", height = 1, 
          width = 2)  
Button_8.configure(font=myFont, fg = "black")
Button_8.grid(row = 0, column = 0,padx = padx_number, sticky=N) 

Button_1 = Button(Frame_2, text = " 9 " , fg = "gray55", height = 1, 
          width = 2)  
Button_1.configure(font=myFont, fg = "black")
Button_1.grid(row = 1, column = 0,padx = padx_number, sticky=N) 

Button_2 = Button(Frame_2, text = " 9 " , fg = "gray55", height = 1, 
          width = 2)  
Button_2.configure(font=myFont, fg = "black")
Button_2.grid(row = 2, column = 0,padx = padx_number, sticky=N) 

# Button_9 = Button(root, text = " 7 " , fg = "gray55", height = 2, 
#           width = 2)  
# Button_9.configure(font=myFont, fg = "black")
# Button_9.grid(row = 0, column = 2,padx = padx_number) 

# Button_1 = Button(root, text = " 7 " , fg = "gray55", height = 1, 
#           width = 2) 
# Button_1.configure(font=myFont, fg = "black")
# Button_1.grid(row = 0, column = 3,padx = padx_number) 

# Button_2 = Button(root, text = " 7 " , fg = "gray55") 
# Button_2.configure(font=myFont, fg = "black")
# Button_2.grid(row = 1, column = 3,padx = padx_number) 



# Button_8 = Button(Frame_4, text = " 8 " , fg = "gray55")
# Button_8.configure(font=myFont, fg = "black")  
# Button_8.grid(row = 0, column = 1,padx = padx_number) 

# Button_9 = Button(Frame_4, text = " 9 " , fg = "gray55")
# Button_9.configure(font=myFont, fg = "black")
# Button_9.grid(row = 0, column = 2,padx = padx_number) 

# Button_x = Button(Frame_4, text = " X " , fg = "gray55")
# Button_x.configure(font=myFont, fg = "black")
# Button_x.grid(row = 0, column = 3,padx = padx_number) 


# Button_4 = Button(Frame_3, text = " 4 " , fg = "gray55") 
# Button_4.configure(font=myFont, fg = "black")
# Button_4.grid(row = 0, column = 0,padx = padx_number)  

# Button_5 = Button(Frame_3, text = " 5 " , fg = "gray55") 
# Button_5.configure(font=myFont, fg = "black")
# Button_5.grid(row = 0, column = 1,padx = padx_number)  

# Button_6 = Button(Frame_3, text = " 6 " , fg = "gray55") 
# Button_6.configure(font=myFont, fg = "black")
# Button_6.grid(row = 0, column = 2,padx = padx_number) 

# Button_m = Button(Frame_3, text = " - " , fg = "gray55")
# Button_m.configure(font=myFont, fg = "black")
# Button_m.grid(row = 0, column = 3,padx = padx_number) 



# Button_1 = Button(Frame_2, text = " 1 " , fg = "gray55")
# Button_1.configure(font=myFont, fg = "black")
# Button_1.grid(row = 0, column = 0,padx = padx_number)  

# Button_2 = Button(Frame_2, text = " 2 " , fg = "gray55")
# Button_2.configure(font=myFont, fg = "black")
# Button_2.grid(row = 0, column = 1,padx = padx_number) 

# Button_3 = Button(Frame_2, text = " 3 " , fg = "gray55")
# Button_3.configure(font=myFont, fg = "black")
# Button_3.grid(row = 0, column = 2,padx = padx_number)  

# Button_p = Button(Frame_2, text = " + " , fg = "gray55")
# Button_p.configure(font=myFont, fg = "black")
# Button_p.grid(row = 0, column = 3,padx = padx_number) 


# Button_0 = Button(Frame_1, text = " 0 " , fg = "gray55")
# Button_0.configure(font=myFont, fg = "black")
# Button_0.grid(row = 0, column = 1,padx = padx_number) 

# Button_00 = Button(Frame_1, text = " , " , fg = "gray55")
# Button_00.configure(font=myFont, fg = "black")
# Button_00.grid(row = 0, column = 2,padx = padx_number) 

# Button_e = Button(Frame_1, text = " = " , fg = "gray55")
# Button_e.configure(font=myFont, fg = "black")
# Button_e.grid(row = 0, column = 3,padx = padx_number)








































root.mainloop()