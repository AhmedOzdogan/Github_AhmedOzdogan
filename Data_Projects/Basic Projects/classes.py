# -*- coding: utf-8 -*-

#%% Basics
class matematik:
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def plus(self):
        return self.num1+self.num2
    
    def minus(self):
        return self.num1-self.num2
    
    def multi(self):
        return self.num1*self.num2
    
    def division(self):
        return self.num1/self.num2

math1 = matematik(1,10)
math2 = matematik(1,11)

print("Result is = " + str(math2.minus()))

#%% Property

class person:
    def __init__(self,fName,lName,age):
        self.fName = fName
        self.lName = lName
        self.age = age
        
        
person1 = person("Ahmed","Özdoğan","23")

print(person1.fName + " "+ person1.lName)
        
class worker(person):
    def __init__(self,salary):
        self.salary = salary
        
class customer(person):  #inherit ederek ilk klastaki tanımları diğer klaslara aktardık. Parantez içine o class'ın adını yazıyoruz.
    def __init__(self,cNumber):
        self.cNumber = cNumber
        
ahmed = worker("0")

ahmed.fName = "Ahmed"
ahmed.lName = "Ozdagan"
ahmed.age = "23"

print(ahmed.lName)

