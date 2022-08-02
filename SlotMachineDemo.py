"""This is slot machine game."""
"""First, the class is created to play with different types of symbols instead of having one."""

import random

class SlotMachine():
    
    items = []
    firstLine = []
    secondline = []
    thirdLine = []
    cash = 1000
    """We have three lines and 1000 cash in the beginning """
    
    def __init__(self,item_1,item_2,item_3,item_4,item_5,item_6,item_7):
        self.item_1 = item_1
        self.item_2 = item_2
        self.item_3 = item_3
        self.item_4 = item_4
        self.item_5 = item_5
        self.item_6 = item_6
        self.item_7 = item_7
        self.items.append(self)

    def fill(self,list1):
        """with this function, we fill the lines. We use random to generate different numbers and 
        , these numbers are used to choose objects."""
        for x in range(3):
            randomNum = random.randint(0, 6)
            list1.append(list(self.__dict__.values())[randomNum])
    
    def start(self):
        """This is the start command. This class the fill function and the game begins."""
        self.fill(self.firstLine)
        self.fill(self.secondline)
        self.fill(self.thirdLine)
        


a = SlotMachine("8","9","10","Q","K","A","Bonus")



a.start()

print(a.firstLine)
print(a.secondline)
print(a.thirdLine)

