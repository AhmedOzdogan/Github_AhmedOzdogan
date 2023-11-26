# -*- coding: utf-8 -*-

import mathModule #diğer modulün adı

mathModule.multi(2,3)
mathModule.plus(5,7)

import mathModule as mm #rename ederek daha sonra mm ile kullanırız

mm.plus(3,5)

print(mm.customers["firstName"]) #listeleride çekebiliriz


from mathModule import multi #sadece o fonksiyonu çağırdık. Hepsini çağırmadık.

multi(3,5)

from mathModule import customers #tekrar mm. veya mathModule. yazmamıza gerek yok.

print(customers["firstName"])

