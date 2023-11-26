# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:31:32 2020

@author: Ahmed
"""

import sqlite3

def joinOp():
    connection = sqlite3.connect("chinook.db")
    
    cursor = connection.execute("""select Albums.title, artists.Name 
                                from artists inner join albums 
                                on artists.ArtistId = albums.ArtistId""")
    for row in cursor:
        print("Title = " + row[0])
        print("Name = " + row[1])
        print("*********")
    
    connection.close()
    
joinOp()

