# -*- coding: utf-8 -*-

# 1 4 7
# 2 5 1


# 8 1 2
# 7 1 3


num1 = (input("Number 1 please ?"))

num2 = (input("Number 2 please ?"))

num3 = (input("Number 3 please ?"))

num4 = (input("Number 4 please ?"))

print(num1)
print(num2)
print(num3)
print(num4)

listNum1 = [int(d) for d in num1]
listNum2 = [int(d) for d in num2]
listNum3 = [int(d) for d in num3]
listNum4 = [int(d) for d in num4]

a = str((int(listNum1[0]) +int(listNum3[0])))
b = str((int(listNum1[1]) +int(listNum3[1])))
c = str((int(listNum1[2]) +int(listNum3[2])))
d = str((int(listNum2[0]) +int(listNum4[0])))
i = str((int(listNum2[1]) +int(listNum4[1])))
f = str((int(listNum2[2]) +int(listNum4[2])))

print(a+","+b+","+c)
print(d+","+i+","+f)






