# -*- coding: utf-8 -*-"""

import sqlite3

def  updateCustomers():

    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city='İstanbul' 
                       where city = 'Ankara'""")
    connection.commit()
    connection.close()
    
    #ankaraları istanbul olarak değiştirdik.

updateCustomers()


