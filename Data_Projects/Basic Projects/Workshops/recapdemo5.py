# -*- coding: utf-8 -*-

import sys #hata kodunu görücez.


list = [7,'Engin',0,3,"6"]

for x in list:
    try:
        print("Sayı : " + str(x))
        outCome = 1/int(x)
        print("Sonuç : " + str(outCome))
    except ValueError:
        print(str(x) + " Bu Bir Sayı Değil")
    except ZeroDivisionError:
        print(str(x) + " : Bir sayı sıfıra bölünemez")
    except:
        print(str(x) + " : Hesaplanamadı")
        print("Hata Kodu : " + str(sys.exc_info()[0])) #try verdik, olmadı hata verdi ve bize hangi hatayı vediğini öğrendik.
    finally:
        #try ve exceptten hangisi çalışırsa çalışsın bu bloğu çalıştırır. Örneğin sql de dosya her halukarda close ile kapatılabilir.
        print("İşlem bitti.")
        
