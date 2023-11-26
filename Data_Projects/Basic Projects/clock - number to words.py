# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 05:46:40 2021

@author: ahmed
"""

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

def n2w(n):
    try:
        return (num2words[n].lower())
    except KeyError:
        try:
            return (num2words[n-n%10].lower() + " " + num2words[n%10].lower())
        except KeyError:
            return ('Number out of range')

m = 1
h = 1
if (m == 0):
    print(n2w(h) + " o'clock")
elif(m == 15):
    print("quarter past " + n2w(h))    
elif(m < 30):
    print(n2w(m) + " minutes past " + n2w(h))
elif(m == 30):
    print("half past " + n2w(h))
elif(m == 45):
    print("quarter to " + n2w(h+1))
else:
    a = 60-m
    print(n2w(a) + " to " + n2w(h+1))