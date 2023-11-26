# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute(""" select FirstName,LastName 
                            from Customers where FirstName like'%a%'""")
                            
#içinde a geçenler

for row in cursor:
    print("First Name = " + row[0])
    print("Last Name = " + row[1])
    print("**********")
    
print("\n")
print("***** - ****** - *****")
print("\n")

cursor1 = connection.execute(""" select FirstName,LastName 
                            from Customers where FirstName like'a%'""")
                            
                        
#ile başlayanlar

for row in cursor1:
    print("First Name = " + row[0])
    print("Last Name = " + row[1])
    print("**********")

print("\n")
print("***** - ****** - *****")
print("\n")

cursor1 = connection.execute(""" select FirstName,LastName 
                            from Customers where FirstName like'%a'""")
                            
                        
#ile bitenler

for row in cursor1:
    print("First Name = " + row[0])
    print("Last Name = " + row[1])
    print("**********")


