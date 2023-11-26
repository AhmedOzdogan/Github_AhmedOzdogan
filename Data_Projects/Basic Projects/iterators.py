# -*- coding: utf-8 -*-

cities = ["Ankara","İstanbul","İzmir"]

iterator = iter(cities)

print(next(iterator))
print(next(iterator))
print(next(iterator)) #her print dediğimide farklı bir iterator yazacak.

for x in cities:
    print(x)  #for da tek tek dönüyoruz. İterator de ise her print de sonrakini tek tek yazdırıyoruz.
