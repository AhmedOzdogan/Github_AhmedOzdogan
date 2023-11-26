#Setler
#performanslıdır ama aynı tip veri bulundurumazlar. Sözlük örnektir. 
#Setler çok daha hızlıdır, elaman değiştirilemez (ama silinir veya eklenir) ve sıralı değiller. İndex giremeyiz. Elamanların sıraları yok. Kendi sıralar.
#kıvırcık parantez.

studentsSet = {"Engin", "Derin", "Salih", "Mehmet", "Mustafa"}

print(studentsSet)

for student in studentsSet:
    print(student)
    
print("Derin" in studentsSet) #true or not?

if "Derin" in studentsSet:
    print("listede var")


studentsSet.add("Ali") # eklemek için

print(studentsSet)

studentsSet.update(["merve","kazım"]) #çoklu eklemek için

print(studentsSet)

print(len(studentsSet))

studentsSet.remove("Derin") #silmek için.

print(len(studentsSet))

studentsSet.discard("Derin") #sil ama bulamazssan bana hata verme geç gitsin.

print(len(studentsSet))

print(studentsSet)

x = studentsSet.pop() # Son elemanı siler. Random olarak siler çünkü index bilmiyoruz. Tehlikeli

print(len(studentsSet))
    
print(studentsSet)

studentsSet.clear() # komple sildi. İçini boşalttı

print(len(studentsSet))

# del studentsSet #komple seti sildi. O yüzden bulamadım diye hata verdi.

# print(len(studentsSet))

studentsSet2 = set("Mehmet")
    
    