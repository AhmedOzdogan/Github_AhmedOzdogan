
alphabet = {
        'a' : 1, 
        'b' : 2, 
        'c' : 3, 
        'd' : 4, 
        'e' : 5, 
        'f' : 6, 
        'g' : 7, 
        'h' : 8, 
        'i' : 9, 
        'j' : 10, 
        'k' : 11, 
        'l' : 12, 
        'm' : 13, 
        'n' : 14, 
        'o' : 15, 
        'p' : 16, 
        'q' : 17, 
        'r' : 18, 
        's' : 19, 
        't' : 20, 
        'u' : 21, 
        'v' : 22, 
        'w' : 23, 
        'x' : 24, 
        'y' : 25, 
        'z' : 26
    }

try:
    number = int(input("How many words do you have?"))
    wordList = []
    counterList =[]

    for x in range(number):
        wordList.append(input("Words please").lower())
    
    for x in wordList:
        counter = 0
        for y in range(len(x)):
            counter = counter + alphabet[x[y]]
        counterList.append(counter)
    
    biggest = wordList[counterList.index(max(counterList))]  
    smallest = wordList[counterList.index(min(counterList))] 
    
    print("Biggest word is " + biggest.capitalize())
    print("Smallest word is " + smallest.capitalize())
except:
    print("Please just provide a number")






    

    
