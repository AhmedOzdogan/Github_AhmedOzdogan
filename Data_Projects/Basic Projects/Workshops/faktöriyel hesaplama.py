# -*- coding: utf-8 -*-


def cal(number):
    i = 1
    j = 1
    for number in range(int(number)):
        j = j*(i)
        i +=1
        if i == number:
            break
    print(j)
    return "Bitti"

num = int(input("Number Please?"))

if num<0:
    print("none")
else:
    print(cal(num))
