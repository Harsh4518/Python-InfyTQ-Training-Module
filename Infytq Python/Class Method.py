#class method and static method.

class A:

    counter=0
    @classmethod

    def fun(cls,newvalue):

        cls.counter=newvalue

obj=A()
obj.fun(40)
A.fun(50)
print(A.counter)
