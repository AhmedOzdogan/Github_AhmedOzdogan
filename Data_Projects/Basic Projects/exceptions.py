# -*- coding: utf-8 -*-

try:
    num = int(input("Sayı giriniz?"))
except ValueError:
    print("Sayı Girmediniz!") #error tipi ile belirttik.
except (ValueError,ZeroDivisionError)
    print("Sayı Girmediniz!") #error tipleri ile belirttik.
except:
    print("Bir hata oluştu") #try ile dene dedik ve hata alırsa excepte geçti.
        
        #hatanın türüne göre de bir except yazabilirizi.
        
print("Bitti")

messa