"""class A:
    def fun(self):
        print("from A")

class B(A):

    def fun(self):
        print("from B")

class C(A):

    def fun(self):

        print("from C")

class D(B,C):
    pass

d=D()
d.fun()"""

#super return a temp object of imidiate super class.

class Employee:

    def __init__(self,first,last,sal):

        self.fname=first
        self.lname=last
        self.salary=sal

    def fullname(self):

        return self.fname+" "+self.lname

class Developer(Employee):

    def __init__(self,first,last,sal,prog_lang):

        super().__init__(first,last,sal)
        self.language=prog_lang

    def getlanguage(self):

        return self.language

    def fullname(self):

        return self.fname+" "+self.lname+ " The Developer"

dev1=Developer("Mohit","Kumar",15000,"python")
dev2=Developer("deepak","Kumar",25000,"java")
print(dev1.fullname())
        
