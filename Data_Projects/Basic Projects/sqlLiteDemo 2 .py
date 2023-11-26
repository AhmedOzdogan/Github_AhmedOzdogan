# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute(""" select city,count(*) 
                            from Customers group by city
                            order by city""")

for row in cursor:
    print("city = " + row[0])
    print("Count = " + str(row[1]))
    print("**********")
    

    
print("\n")    
print("********* ******** *******")
print("\n") 

cursor1 = connection.execute(""" select city,count(*) 
                            from Customers group by city
                            order by count(*) desc""")

for row in cursor1:
    print("city = " + row[0])
    print("Count = " + str(row[1]))
    print("**********")
    
print("\n")    
print("********* ******** *******")
print("\n") 

cursor2 = connection.execute(""" select city,count(*) 
                            from Customers group by city
                            having count(*)>1
                            order by count(*) desc""") #sadece 1 den büyükleri aldık

for row in cursor2:
    print("city = " + row[0])
    print("Count = " + str(row[1]))
    print("**********")
    


    
    
    
    
   
    
