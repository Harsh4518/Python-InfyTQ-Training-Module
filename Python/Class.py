"""class Mobile:
    pass

M1=Mobile()
M2=Mobile()
print(id(M1),id(M2))"""

"""class Mobile:

    def __init__(self):

        print("Id of self in constructor",id(self))

mob1=Mobile()"""

class Mobile:

    def __init__(self,brand,price):

        print("inside constructor")
        self.brand=brand
        self.price=price
        camera=3

mob1=Mobile("apple",2000)
print(mob1.brand,mob1.price)
print(mob1.__dict__)

