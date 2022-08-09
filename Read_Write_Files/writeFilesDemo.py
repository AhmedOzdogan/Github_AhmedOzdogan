# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:13:33 2022

@author: ahmed
"""

with open("new.txt","a") as file:
    file.write("This is line 4\n")

# with open("new.txt","r") as fileread:
#     File_stuff = fileread.read()
#     print(File_stuff)
#     print(File_stuff)

list1 = ["This is line 5\n","This is line 6\n","This is line 7\n"]
with open("new.txt","a") as file2:
    for x in list1:
        file2.write(x)