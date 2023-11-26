# -*- coding: utf-8 -*-


nums = [1,2,3,4,5]

numsSquare = []

# for x in nums:
#     numsSquare.append(x*x) #her sayının karesi ile farklı bir liste oluşturduk


NumsSquare =list(map(lambda x: x**5,nums)) #for yerine map ile aynı işlemi yaptık.


print(numsSquare)

numsFiltered = list(filter(lambda x: x>2,nums)) #Sadece 2'den büyükleri filtereleyerek içeri aktardık.


print(numsFiltered)

from functools import reduce

numsFactorial = reduce(lambda x,y:x*y,nums) #1*2 den x=2 oldu. Sonra 2*3'dden x = 6 oldu gibi ekleyerek gidiyo
print(numsFactorial)



    

