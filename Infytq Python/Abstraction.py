#Abstraction

from abc import ABC,abstractmethod

class Base(ABC):

    @abstractmethod

    def method(self):

        pass

class Implementation(Base):
    num=10
    def method(self):

        print(self.num)

obj=num.implementation()
print(obj)
        
