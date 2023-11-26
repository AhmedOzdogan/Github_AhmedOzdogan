# -*- coding: utf-8 -*-

students = ["Engin", "Ali", "Ahmed", "Mehmet","Salih"]

fAppend = open("students.txt","a")

for e in students:
    fAppend.write(e)   #Listeyi txt'ye yazdırdık.
    fAppend.write("\n")


fAppend.close()

