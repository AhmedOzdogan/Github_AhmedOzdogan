# -*- coding: utf-8 -*-
j = int(input("Sayı - 1 ?"))

k = int(input("Sayı - 2 ?"))

l = int(input("Sayı - 3 ?"))


if j>k and k>l: #my solution
    print("Biggest Number is " + str(j))

elif j>k and l>j:
    print("Biggest Number is " + str(l))
    
elif j<k and l>k:
    print("Biggest Number is " + str(l))
    
else:
    print("Biggest Number is " + str(k))
    
if j>k and k>l: #my solution
    Biggest = j

elif j>k and l>j:
    Biggest = l
    
elif j<k and l>k:
    Biggest = l
    
else:
    Biggest = k

print(str(Biggest))
    

    


