# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:17:20 2020

@author: Ahmed
"""


import json

with open("users.json") as users: #dosyayı açtık
    data = json.load(users) #data diye okuduk
    
    
    for x in range (5):
        
        print(data[x]["username"]) #adını gördük
        print(data[x]["email"]) # emailini gördüj
        print(data[x]["address"]["street"]) #sokağını gördük
        print(data[x]["address"]["geo"]["lat"]) #kordinatinı gördük
        