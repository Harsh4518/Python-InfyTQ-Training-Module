#user defined exception.
#for creating a user defined exception we create a seperate exception class.
#for creating a user defined exception we create a class than inherit exception class.

class PriceException(Exception):
    pass
class CardException(Exception):
    pass
def purchase_item(price,cardno):
    if price<0:
        raise PriceException("invalid price")
    if cardno not in [101,102,103,104,105]:
        raise CardException("wrong card")

try:
    purchase_item(-1200,100)
except PriceException as e:
    print("Product price is wrong",e)
except CardException as e:
    print("invalid card",e)

#no underscore-public
#single underscore0-private
#double underscore-protected

class NotEligibleException(Exception):

    pass

class Employee:

    def __init__(self,salary):
        
        self._salary=salary
    
    def check_salary(self):

        try:
            if (self._salary<2000):
                raise NotEligibleException
            else:
                return True
        except NotEligibleException:
            print("1")
            raise NotEligibleException

emp1=Employee(1000)

try:
    status=emp1.check_salary()
    print("2")
except NotEligibleException:

    print("3")

#assert-used to raise assertion error
#after assert keyword we write boolean keyword.
#if the boolean statement is true than we continue to execute next line otherwise an assertion error exception is raised and corresponding message is raised.

"""def KelvinToFahrenheit(Temperature):

    assert(Temperature>=0)
    return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(KelvinToFahrenheit(505.78))
print(KelvinToFahrenheit(-5))"""

#computer based Numerical Statistical Technique.

#newton raphson's method:
 
#Xn+1=Xn-f(Xn)/f'(Xn)
        
#newtons method for square root of a number.]

#Xn+1=1/2[Xn+a/Xn]

x=9
a=25
while 1:

    xnew=0.5*(x+a/x)

    if abs(xnew-x)<0.00000000001:
        break
    x=xnew

print(x)
















