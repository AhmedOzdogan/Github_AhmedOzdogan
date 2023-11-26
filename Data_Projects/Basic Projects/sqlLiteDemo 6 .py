# -*- coding: utf-8 -*-

import sqlite3

def  deleteCustomers():

    connection = sqlite3.connect("chinook.db")
    connection.execute("""delete from customers 
                       where customerid = 60""")
    connection.commit()
    connection.close()
    
    #ankaraları istanbul olarak değiştirdik.

deleteCustomers()