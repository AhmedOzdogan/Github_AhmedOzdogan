"""
First Project

"""

print("Welcome to the My New Project")

i = input("İlk olarak adınız ?")

j = input("ve yaşınız ?")

print("Cevaplar için teşekkür ederim")

k = input("Kişisel bilgilerinizi paylaşmaya devam etmek istiyor musunuz? Y/N")

if(k == "N"):
    print("Görüşmek üzere")
else:
    l= 2020-int(j)
    print("Doğum tarihinizin " + str(l) + " olduğunu var sayar ise doğum aynızı tahmin etmeye çalışacağım")
    
    p = "Çok da zor olmadı :)"
    n = "Daha erken Bulmam gerekirdi"
    o ="Sonunda :/"
    
    print("Aralık mı?")
    m = input("Y/N")
    
    if (m == "Y"):
        print(p)    
    else:
        print("Ocak mı?")
        m = input("Y/N")
    
        if (m == "Y"):
            print(p)    
        else:  
            print("Haziran mı?")
            m = input("Y/N")
    
            if (m == "Y"):
                print(p)    
            else:
                print("Kasım mı?")
                m = input("Y/N")
    
                if (m == "Y"):
                    print(p) 
                else:
                    print("Şubat mı?")
                    m = input("Y/N")
                
                    if (m == "Y"):
                        print(n)
                    else:
                        print("Mart mı?")
                        m = input("Y/N")
                    
                        if (m == "Y"):
                            print(n)
                        else:
                            print("Mayıs mı?")
                            m = input("Y/N")
                        
                            if (m == "Y"):
                                print(n)
                            else:
                                print("Temmuz mı?")
                                m = input("Y/N")
                            
                                if (m == "Y"):
                                    print(n)
                                else:
                                    print("Eylül mı?")
                                    m = input("Y/N")
                                
                                    if (m == "Y"):
                                        print(o)
                                    else:
                                        print("Nisan mı?")
                                        m = input("Y/N")
                                    
                                        if (m == "Y"):
                                            print(o)
                                        else:
                                            print("Ağustos mu?")
                                            m = input("Y/N")
                                        
                                            if (m == "Y"):
                                                print(o)
                                            else:
                                                print("Ekim mı?")
                                                m = input("Y/N")
                                            
                                                if (m == "Y"):
                                                    print(o)

    print("Sırada doğum gününüz var")
    
    numbers = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
    "22","23","24","25","26","27","28","29","30","31"]
    for x in numbers:
        print(x)
        if x == "12" :
            break

            
        

    
       