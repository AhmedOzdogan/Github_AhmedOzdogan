# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 10:37:19 2022

@author: ahmed
"""

file = open("new.txt","r")

print(file.name)
print(file.mode)
# file.close()
print(file.close())


with open("new.txt","r") as file1:
    """automatically closes"""
    File_stuff = file1.read()
    """we can only read in an indented block"""
    print(File_stuff)
print(file1.closed)
print(File_stuff)

print("***")

with open("new.txt","r") as file2:
    file_stuff = file2.readlines()
    print(file_stuff)

print("***")

with open("new.txt","r") as file3:
    file_stuff = file3.readline()
    print(file_stuff)
    file_stuff = file3.readline()
    print(file_stuff)
    file_stuff = file3.readline()
    print(file_stuff)
    
print("***")

with open("new.txt","r") as file4:
    file_stuff = file4.read(14)
    print(file_stuff)
    file_stuff = file4.read(9)
    print(file_stuff)
    file_stuff = file4.read(6)
    print(file_stuff)
    
print("***")

