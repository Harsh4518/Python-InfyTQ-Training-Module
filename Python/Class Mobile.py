class Mobile:

    def __init__(self,brand,price):

        print("inside constructor")
        self._brand=brand
        self._price=price
        camera=3

    def getbrand(self): #getter function

        return self._brand

    def getprice(self):

        return self._price

    def set_price(self,p): #setter function

        self._price=p

mob1=Mobile("Apple",20000)
print(mob1.getbrand())
print(mob1.getprice())
mob1.set_price(30000)
print(mob1.getprice())
print(mob1.__dict__)
