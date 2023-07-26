#class Method and static handle

class A:

    counter=0
    #Decorator function accessed by object and class name both.
    @staticmethod
    def fun(newval):

        A.counter=newval
        print("Normal fun in Class")

obj=A()
obj.fun(1) #correct
A.fun(2) #correct

print(A.counter)

