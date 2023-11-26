# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:08:05 2020

@author: Ahmed
"""

def BinaryReversal(num):
    print(num)
    
    a = int((bin(num).replace("0b","")))

    reverse = 0
    
    while(a > 0):    
        reminder = a % 10
        
        reverse = (reverse * 10) + reminder
        
        a = a // 10  
    
    print(int(str(reverse),2))

BinaryReversal(int(input("number?")))