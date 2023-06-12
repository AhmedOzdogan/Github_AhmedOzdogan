"""This is slot machine game."""
"""First, the class is created to play with different types of symbols instead of having one."""

import random

class SlotMachine():
    
    firstLine = []
    secondLine = []
    thirdLine = []
    cash = 1000
    bet = int1
    """We have three lines and 1000 cash in the beginning """
    
    def __init__(self,item_1,item_2,item_3,item_4,item_5):
        self.item_1 = item_1
        self.item_2 = item_2
        self.item_3 = item_3
        self.item_4 = item_4
        self.item_5 = item_5

    def cont (self) :
         if self.cash == 0:
             print("You lost!!!\n*** Thanks for Playing***")
             
         else:
            a = input("Do you want to continue? y/n")
            
            if a.lower() in ["y","yes"]:
                self.firstLine.clear()
                self.secondLine.clear()
                self.thirdLine.clear()
                self.start()           
            else:
                print("*** Thanks for Playing***")
                print("Final is " + str(self.cash))
            
             

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
        """we will check whether you win or lose by counting the three objects in every single line"""
        win = 0
        fulllist = []
        results1 = []
        results2 = []
        results3 = []
        
        for x in (self.firstLine,self.secondLine,self.thirdLine):
            results1.extend(x)
        
        fulllist.extend(self.firstLine)
        fulllist.extend(self.secondLine)
        fulllist.extend(self.thirdLine)

        if fulllist.count(list(self.__dict__.values())[4]) >3:
            win = self.bet * fulllist.count(self.item_5)
            print("Bonus win is " + str(self.bet * fulllist.count(self.item_5) + " with " + self.item_5))
            
        for x in(0,3,6):
            for y in (1,4,7):
                for z in (2,5,8):
                    c = []
                    
                    c.append(results1[x])
                    c.append(results1[y])
                    c.append(results1[z])
                    results2.append(set(c))
                    
        for i in results2:
            if len(i)== 1 and i:
                results3.append(i)

        
        for x in results3:
            if list(x)[0] in list(self.__dict__.values())[3:5] :
                win = win + self.bet*2
                print("You win " + str(self.bet*2) + " with " + str(list(x)[0]) +" line!!!")
            else:
                win = win + self.bet
                print("You win " + str(self.bet) + " with " + str(list(x)[0]) +" line!!!")
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
b = SlotMachine("Apple","Orange","Cherry","Kiwi","Wild")

print("Welcome to the Game \nGood Luck!")
choice = input("we have two sets availbale \nyou can either play with cards or fruits.\n(1 for deck, 2 for fruits)")

if choice == "1":
    a.start()
elif choice == "2":
    b.start()
else:
    print("invalid input!!!\nPlease try again later!")



