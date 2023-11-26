# -*- coding: utf-8 -*-


from tkinter import *

root = Tk() # we created a window

theLabel = Label(root, text="Ahmed") #we put a label in it, first we declare where the label belongs and then the text

theLabel.pack() #ekrana uyguladık.

root.mainloop() # bunu yazmazsak açıp ve kapattı. Ama bunu yazınca loop yarattı.

