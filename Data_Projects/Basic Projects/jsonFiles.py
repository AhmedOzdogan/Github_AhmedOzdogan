# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:05:53 2020

@author: Ahmed
"""

import json

data = '{"firstName" : "Ahmed", "LastName" : "Ozdogan"}'

y= json.loads(data) #bir stringi Json'a çevirdik

print(type(data))

print(y["firstName"])

customers = {
    "fName" : "Ahmed",
    "email" : "ahmed@com"    
    }


customersJson = json.dumps(customers) #bir dictionary'i jsona çevirdik.

print(customers)

print(json.dumps("Ahmed"))