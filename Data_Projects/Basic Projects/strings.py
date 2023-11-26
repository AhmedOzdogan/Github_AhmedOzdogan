message = "Hello World!"

#creating substrings

print(message[2:5]) #from 2 to 5

newMessage = message[2:5]

print(newMessage)
print(message[2:]) #from 2 ...
print(message[:5]) #until 5

#identify the lenght of String

print(len(message))

print(message[len(message)-1:])
newMessage2 = message[len(message)-1:]

print(newMessage2)

#lower - upper / ascii code

print(message.upper())
print(message.lower())

firstString = message.upper()
secondString = message.lower()

print(firstString+secondString)

print(firstString[len(message)-len(message)]+
      secondString[len(message)-(len(message)-1)]+
      firstString[len(message)-(len(message)-2)]+
      secondString[len(message)-(len(message)-3)]+
      firstString[len(message)-(len(message)-4)]+
      secondString[len(message)-(len(message)-5)]+
      firstString[len(message)-(len(message)-6)]+
      secondString[len(message)-(len(message)-7)]+
      firstString[len(message)-(len(message)-8)]+
      secondString[len(message)-(len(message)-9)]+
      firstString[len(message)-(len(message)-10)]+
      secondString[len(message)-(len(message)-11)]
      )

print(message.replace("e","a")) #can be useful for turkish character

info = "   Ahmed Özdoğan 23 Ankara"

#split() splitting a string for a certain character

print(info.split())
print(info.split(" ")) #split with space
print("Name :" + info.split()[0]) #split and choose
print("Age: " + info.split()[2])

#input

name = input("Name?")

sayi1 = input("sayi 1 = ?")
sayi2 = input("sayi2 = ?")

print(int(sayi1)+int(sayi2)) #we chanced its format to integer /str /float


