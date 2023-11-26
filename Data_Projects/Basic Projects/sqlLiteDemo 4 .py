# -*- coding: utf-8 -*-
import sqlite3


def  insertCustomers():

    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers 
                       (firstName,lastName,city,email) 
                       values ('Sibel','Ozdogan','Ankara','sibel@gmail.com')""")
    connection.commit()
    connection.close()

insertCustomers()

#emailsiz yazarsak uyarı alırız. Çünkü E-mail zorunlu bir alan.
