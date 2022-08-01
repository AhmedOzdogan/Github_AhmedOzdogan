class Company(object):
    employeesCount = 0
    employeesList = []
    
    def __init__(self,name ,surname ,salary ,position):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name+surname + "@mail.com"
        self.position = position
        Company.employeesCount += 1
        Company.employeesList.append(''.join(self.name + " " + self.surname))
        
    def salary_increase(self,percent):
        self.salary = self.salary*(100+percent)/100
        return(self.salary)
    
    def salary_decrease(self,percent):
        self.salary = self.salary*(100-percent)/1000

emp1 = Company("Ahmed","Ozdogan",13000,"COO")
emp2 = Company("Jack","Simmons",12200,"Manager")
emp3 = Company("Linda","Broke",9500,"Front Desk")

emp1.salary_increase(10)

emp3.salary_decrease(10)

names = ["Michael","John","Amy","Stella","Peter"]
surnames = ["Done","Geniune","Star","Brick"]


nameList = []
for x in names:
    tempList = []
    for y in surnames:
        tempList.append(x)
        tempList.append(y)
        nameList.extend(tempList)
        tempList.clear()

def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

nameList = split(nameList,2)

for x in range(len(nameList)):
    nameList[x].append(5000)
    nameList[x].append("Servant")


d = {}
for x in range(4,len(nameList)+4):
    d['emp{0}'.format(x)] = nameList[x-4]

print(d["emp4"])
# for x in d:
#     x = Company(d[x])