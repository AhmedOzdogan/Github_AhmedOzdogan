#first key, ikincisi value
dictionary = {
    "book" : "kitap",
    "table" : "masa"    
    }

dictionary2 = dict(
    kitap = "book",
    masa = "table"
    ) #another version of dictionary

print(dictionary["book"])

dictionary["book"] = "kitap1" #chance the value

print(dictionary["book"])

dictionary["pencil"] = "kalem" #add key

print(dictionary["pencil"])

# del(dictionary["book"]) #delete a key

# print(dictionary["book"])

print(dictionary)
print(len(dictionary))

