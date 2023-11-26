
# cities = "Ankara"

# print(cities.find("a"))

def sayHi(name):
    print("Hi " + name + ", How are you?")
    
sayHi("Ahmed")
    
def dikUcgenAlaniHesapla(a,b):
    return a*b/2

#%%

print(dikUcgenAlaniHesapla(5,4))

#%%

dikUcgenAlaniHesapla2 = lambda a,b : a*b/2 #lambda kullanırken fonskiyonu yazmadığın sürece parantez açıp kapatmana gerek yok.

print(dikUcgenAlaniHesapla2(3,6))

print(type(dikUcgenAlaniHesapla2))

x = dikUcgenAlaniHesapla2

print(x(10,20))