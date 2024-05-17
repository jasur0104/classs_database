class Animal:
    def __init__(self,name,age,id,passport):
        self.name = name
        self.age = age
        self.id=id
        self.passport = passport
        def sound():
            a=input("""
            qaysi hayvon ni ovozini eshitmoqchisz
            1.kuchuk
            2.mushuk
            3.sigir
            4.eshshak
            >>>""")
            if a=='1':
                print("wow wow wow wow")
            elif a=='2':
                print("miyov miyov miyov")
            elif a=='2':
                print("moooooooo")
            elif a=='3':
                print("ioooooo ioooo")
            else:
                print("error")
        def nameE(self):
            print(self.name)




kuchuk=Animal("rokki",23,"<NAME>",True)
mushuk=Animal("asal",22,"<NAME>",False)
sigir=Animal("uthor",21,"<NAME>",True)
eshshak=(Animal("kuchli",23,"<NAME>",False)