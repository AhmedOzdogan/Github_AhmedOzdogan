#tuple yuvarlar parantez unutma ve değiştirilemezler, buda performans sağlar çünkü sadece read-on dosyalardır.

tupleliste = (2,4,6,"Ankara",(2,3,4),())

liste = [2,4,6,"Ankara",[3,4,5],[]]

#tuple içine liste, liste içine tuple koyulabilir.

liste[0] = 6
#tupleliste[0] = 6

tupleDeger =("Ahmed",) 

print(tupleDeger) 

print(type(tupleDeger))

print(type(tupleliste))
print(liste[1:2])
print(tupleliste[1:2]) #virgüllü verdi, çünkü tek eleman geldiğinde yanına virgül koyar ki normal stringle karıştırılmasın
                        #bizde üstte olduğu gibi sonuna virgül koyarsak onu tuple olarak tanıtırız.


print(liste[-2])
print(tupleliste[-2])



print(type(tupleliste))

print(type(liste))

print(len(tupleliste))

print(len(liste))

print(tupleliste)

print(liste)

