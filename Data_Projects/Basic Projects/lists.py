# ogrenci1 = "Engin"
# ogrenci2 = "Derin"
# ogrenci3 = "Salih"

students = ["Engin", "Derin", "Salih"]

print(students)

students.append("Ahmet") #Add

students[2] = "Veli" #change

students.remove("Engin") #remove
print(students)

#List Constructor
cities = list(("Ankara","İstanbul", "İzmir"))

print(cities)

print(len(cities))

#others functions

#print(cities.clear()) #delete all componenets


print(cities.count("Ankara")) #number of componenets

print("Ankara sayısı = " + str(cities.count("Ankara"))) #how many ankara

print("Ankara indexi = " + str(cities.index("Ankara"))) #place  number

#cities.pop(1) #remove component for its index number

#cities.insert(0,"İzmir") #change components place 


cities.reverse() #change like mirror(tam tersine çevirir.)

print(cities)

cities2=cities

cities3 = cities.copy()  #make a copy, so when you change the cities, it wont affect the cities 3

cities2[0]="Diyarbakır"

print(cities)
print(cities2) #diziler referans tiptir. Birini değiştirirsen ikiside değişir.
print(cities3)

cities.extend(cities3) #extending groups

cities.sort() #sorting A-Z

print(cities)

cities.reverse()

print(cities)

