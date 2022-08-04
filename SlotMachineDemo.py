"""This is slot machine game."""
"""First, the class is created to play with different types of symbols instead of having one."""

import random

class SlotMachine():
    
    items = []
    firstLine = []
    secondLine = []
    thirdLine = []
    cash = 1000
    bet = int
    """We have three lines and 1000 cash in the beginning """
    
    def __init__(self,item_1,item_2,item_3,item_4,item_5):
        self.item_1 = item_1
        self.item_2 = item_2
        self.item_3 = item_3
        self.item_4 = item_4
        self.item_5 = item_5

        self.items.append(self)
        
    def cont (self) :
        
        a = input("Do you want to continue? y/n")
        
        if a.lower() in ["y","yes"]:
            self.firstLine.clear()
            self.secondLine.clear()
            self.thirdLine.clear()
        else:
            print("*** Thanks for Playing***")
            print("Final is " + str(self.cash))
            
            self.start()            

    def fill(self,list1):
        """with this function, we fill the lines. We use random to generate different numbers and 
        , these numbers are used to choose objects."""
        for x in range(3):
            randomNum = random.randint(0, 4)
            list1.append(list(self.__dict__.values())[randomNum])
    
    def result(self,win):
        
        if win > 0:
            
            print("*** Total win is " + str(win) + "***")
            print("You have " + str(self.cash))
            
        else:
            print("you lost")
            print("you have " + str(self.cash))
        
        
        print(self.firstLine)
        print(self.secondLine)
        print(self.thirdLine)
        
        self.cont()
    
    def checker(self):
        win = 0
        fulllist = []
        
        fulllist.extend(self.firstLine)
        fulllist.extend(self.secondLine)
        fulllist.extend(self.thirdLine)

        if fulllist.count(list(self.__dict__.values())[-1]) >2:
            win = self.bet * fulllist.count(list(self.__dict__.values())[-1])
            print("Bonus win is " + str(self.bet * fulllist.count(list(self.__dict__.values())[-1])))
            

        for x in (self.firstLine[0],self.secondLine[0],self.thirdLine[0]):
            index = 1

            if x == self.firstLine[index] or x == self.secondLine[index] or x == self.thirdLine[index]:
                index +=1
                
                if x == self.firstLine[index] or x == self.secondLine[index] or x == self.thirdLine[index]:
                    if x in (list(self.__dict__.values())[:2]):
                        win = win + self.bet*2
                        print( x + " line win is " + str(self.bet*2))
                    else:
                        win = win + self.bet*4
                        print( x + " line win is " + str(self.bet*4))
                        

        if win == 0 :
            self.cash = self.cash - self.bet

                    
        self.cash = win + self.cash
        
        self.result(win)
                    
    def start(self):
        """This is the start command. This class the fill function and the game begins."""
        
        self.bet = int(input("how much would you like to bet?"))
        self.fill(self.firstLine)
        self.fill(self.secondLine)
        self.fill(self.thirdLine)
        
        self.checker()
        


a = SlotMachine("J","Q","K","A","Bonus")

a.start()



