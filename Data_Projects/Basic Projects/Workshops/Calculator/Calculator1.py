# -*- coding: utf-8 -*-

print("Hesap Makinesine Hoşgeldiniz")

print("işlem Nedir ?")

print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")

isl1 = input("Lütfen işlemi belirtiniz?")

isl2 = input("İlk sayıyı belirtiniz?")


isl3 = input("ikinci sayıyı belirtiniz?")

from Calculator2 import matematik

math1 = matematik(int(isl2),int(isl3))

 
if isl1 == "1":
    print("Sonuç : " + str(math1.plus()))
elif isl1 == "2":
    print("Sonuç : " + str(math1.minus()))
elif isl1 == "3":
    print("Sonuç : " + str(math1.multi()))
elif isl1 == "4":
    print("Sonuç : " + str(math1.division()))
else:
    print("Tanımlanmayan bir işlem girdiniz !!")
    
    




