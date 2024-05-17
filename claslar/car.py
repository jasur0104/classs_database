class Car:
    def __init__(self, color, model, year,price):
        self.color = color
        self.model = model
        self.year = year
        self.price =price
    def get_color(self):
        a=int(input("mqshina narxini qanchaga uzgartiramiz:"))
        return self.price+a
nexia2=Car("red","nexia2 legenda","2017",10000)
bmw=Car("blue","bmw","2017",13000)
malibura=Car("red","malibura",2018,23000)
print(nexia2.get_color())

