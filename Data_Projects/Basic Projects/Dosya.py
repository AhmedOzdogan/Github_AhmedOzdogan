# # -*- coding: utf-8 -*-

# f = open("customers.txt") 

# # print(f.read(10)) #sayı girersek o kadar karakter okur.

# # r okumak için

# # a üzerine eklemek için

# # w write için

# # x'de oluşturmak için, aynı isimde dosya varsa hata verir.

# #defolut r'dir.

# # print(f.readline()) #sadece 1 line okur ama daha önce read komutu yazılmış ise okumaz. Çoklu satır okuması için for kullanılır.

# for l in f:
#     print(l) #herline tek tek okur.,,
    
# f.close()    #dosya ile işimiz bitti kapattık.

# fAppend = open("students.txt","a") #yoksa oluşturur.

# fAppend.write("Derin") #yan yana ekledi.

# fAppend.write("\n") # bir satır aşağı kaydı

# fAppend.write("Salih")

# fAppend.close()

# fAppend2 = open("students2.txt","w") #yoksa oluşturur.

# fAppend2.write("Ahmed") #olan verinin üzerine yazdı. yani replace etti. eklemedi.

# fAppend2.close()

# import os

f3 = open("students3.txt")

f3.close

import os 

if os.path.exists("customers2.txt"): #kontrol eder.
    os.remove("customers2.txt") #siler
else:
    print("file does not exist")
    
os.rmdir("empty") #klasörü komple sildi.

        




         
         

