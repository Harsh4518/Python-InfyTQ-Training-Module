#Python-Interpreted,dynamically typed

x=23
print(x,type(x))
x="hello"
print(x,type(x))

a=23.54
print(a)
print(type(a))
print(id(a))

#complex number

z1=3+4j
z2=1+2j

print(z1+z2)
print(z1-z2)
z3=z1*z2
print(z3)
print(z3.imag,z3.real)

#keyword
import keyword
#print(keyword.kwlist)

#print methods
print(2,3,4,sep="-")

for i in range(5):
    print(i,end="*")

print(5/2)
print(5//2)
print(5.0//2)

print(8%3)
print(-8%3)
print(-7%3)

a,b,c=10,20,30
a-=b+c
print(a)

a,b,c=10,20,30
a=10;b=20;c=30
print(a,b,c)

a=60
b=13
print(a&b)
print(a|b)
print(a^b)

a=60
print(~a) #2s compliment.[-(n+1)]

a=60
print(a<<2) #multiply by 2 to the power times left shifted.->(Number)*(2**no of shifts)
print(a>>2) #divide by 2 to the power times left shifted.->(Number)//(2**no of shifts

#boolfunction
print(bool("hello"))
print(not "hello")
print(not "")
print(0 or "hello" and 1)

#shortcircuiting rule

#always return the evaluated value of the expression

a,c=0,3
x=c or a
print(x)

print({} and [])
print({}or[])
print({1} and [])
print({1} or [])

x=True
y=False
print(x*y)

s="psit"
x="i" in s
print(x)
y="i" not in s
print(y)
z="f" not in s
print(z)

a=20
b=20
print(id(a),id(b))

"""In python every thing is an object therefore variable to a int is just reference to the memory location."""

a=20
b=20
print(id(a),id(b))
print(a is b)

a=b
print(a is b)
print(a is not b)

print(3**1**9) #right to left calculate.

#Python 3.10 match case(Switch-case)....
x="hi"

match x:

    case "hi":
        print("hi harsh")
        
    case "hello":
        print("hello harsh")

    case _:
        print("Nothing")

month='feb'

match month:

    case 'jan'|'march'|'dec':
        print("1")

    case 'feb':
        print("2")

    case _:
        print("nothing")

#while else statement...
        
x=1
while x<=7:

    print(x)
    x+=1
    if x==5:
        break

else:
    print("Out of loop")

x=1
while x<=7:

    print(x)
    x+=1
    if x==5:
        continue

else:
    print("Out of loop")


n=23
for i in (2,n):

    if n%a==0:
        print("not prime")
        break

else:
    print("prime")

a=[1,2,3,4,5]
n=len(a)

if (n)>3:
    print("list is too long",n,"elements expected <=3")

#python 3.8
#walrus operator

a=[1,2,3,4]

if (n :=len(a))>3:
    print("list is too long",n,"elements expected <=3")

import math
print(dir(math))







    
