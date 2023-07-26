#Higher Order Function.

#Decortor
def f(x):

    def f2():

        print("Hello")
        x()

    return f2

def f1():

    print("hi")

f=f(f1)
f()

###################

#1.Map Function

#map(fun,iterable)

l1=[1,2,3,4,5]

def f(n):

    return n*2

r=map(f,l1) #iterate through map object.

for  i in r:

    print(i)

l1=[1,2,3,4,5]
l2=[2,3,4,5,6] #map on two list

def f(n1,n2):

    return n1+n2

r=list(map(f,l1,l2))
print(r)

###################

#2.Filter

l1=[1,2,3,4,5]


def f(n):

    if n%2==0:

        return True

    return False

r=list(filter(f,l1))
print(r)

def f(n):

    return 5

r=list(filter(f,l1))
print(r)

def f(n):

    print("6") #function returns None Zero Value.

r=list(filter(f,l1))
print(r)

def f(n):

    return print("6")

r=list(filter(f,l1))
print(r)

###################

#3.Reduce

from functools import reduce

l1=[1,2,3,4,5]

def f(n1,n2):

    return n1+n2

r=reduce(f,l1,)
print(r)


