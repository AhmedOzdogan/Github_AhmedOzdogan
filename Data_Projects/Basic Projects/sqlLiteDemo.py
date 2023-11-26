# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("chinook.db")


cursor = connection.execute("select * from customers")

#select seç
#* tüm kolonları
# from nerden
#customerstan

for row in cursor:
    print("First Name = " + row[1])

print("\n")    
print("********* ******** *******")
print("\n") 
    

cursor1 = connection.execute("select FirstName,LastName from customers")
    

for row in cursor1:
    print("Name : " + row[0] + " " + row[1])
   
    
    #row 1 dediğimizde first ve last name seçtiğimiz için 1. kolon last name oldu. 0. kolon ise first name
    
print("\n")    
print("********* ******** *******")
print("\n") 
   
cursor2 = connection.execute("select FirstName,LastName from customers where City='Prague'")

#where ile sadece o şarta uyan isimleri yazdırdık
    

for row in cursor2:
    print("Name : " + row[0] + " " + row[1])
    
print("\n")    
print("********* ******** *******")
print("\n") 

cursor3 = connection.execute("select FirstName,LastName from customers where City='Prague' or City='Berlin'")

#or  ile sadece o veya başka bri şarta uyan isimleri yazdırdık
    

for row in cursor3:
    print("Name : " + row[0] + " " + row[1])
    
print("\n")    
print("********* ******** *******")
print("\n") 
    
cursor4 = connection.execute("""select FirstName,LastName 
                             from customers 
                             where City='Prague' or City='Berlin'
                             order by FirstName""")

#"""ile aşağı atabliriz"""
#order by ile sıraladık gelen verileri. sonunda görülmeyen bir asc var ve artan demek
#eğer desc yazarsak ters sıralar.
    

for row in cursor4:
    print("Name : " + row[0] + " " + row[1])

print("\n")    
print("********* ******** *******")
print("\n")
    
cursor5 = connection.execute("""select FirstName,LastName 
                             from customers 
                             where City='Prague' or City='Berlin'
                             order by FirstName desc""")

#"""ile aşağı atabliriz"""
#order by ile sıraladık gelen verileri. sonunda görülmeyen bir asc var ve artan demek
#eğer desc yazarsak ters sıralar.
    

for row in cursor5:
    print("Name : " + row[0] + " " + row[1])

print("\n")    
print("********* ******** *******")
print("\n")
    
cursor6 = connection.execute("""select FirstName,LastName 
                             from customers 
                             where City='Prague' or City='Berlin'
                             order by FirstName,LastName""")

#ilk firstname göre sıraladı, sonra aynı isimleri soy isme göre sıraladı.
    

for row in cursor6:
    print("Name : " + row[0] + " " + row[1])


connection.close()































