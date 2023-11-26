
cities = ["Ankara" , "İstanbul", "İzmir"]

print(len(cities))
print(cities.index("İzmir"))

print(type(len(cities)))

print(type(cities.index("Ankara")))

for x in cities:
    print(x + " için kod " + x[0:3])

def printCities():
    for x in cities:
        if cities.index(x) == len(cities):
            break
        print(x)
        
# continue ise o anki loopunu iptal edip baştan alır.
        
##!= eşit değilse demek
        
print(printCities())
        
    
