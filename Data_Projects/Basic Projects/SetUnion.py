#union işlemi = 1,2,3 ve 3,4,5 setlerini birleşitirerek 1,2,3,4,5 yazar ve 3'ü bir kere yazar

setA = {1,2,3,4,5}

setB = {1,3,4,6,7,8}

print(setA | setB)

print(setA.union(setB))

print(setB.union(setA))

#intersection ile kesişimi bul

print(setA & setB)

print(setA.intersection(setB))

print(setB.intersection(setA))

#difference ise A-B'yi verir . Yani A'da olup B de olmayan.

print(setA - setB)

print(setA.difference(setB))

print(setB.difference(setA))


#Symmetric kullnarak intersection ile gelen kesişimi komple çıkartırız. Yani sadece A da ve B de olanlar,
#A-B + B-A

print(setA ^ setB)

print(setA.symmetric_difference(setB))

print(setB.symmetric_difference(setA))



