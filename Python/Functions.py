###Python Functions:-
##def adds(a,b):
##
##    c=a+b
##    print(c)
##    return
##
##print(adds(3,5))
##
###None is a object of none type class.
##
##def f():
##
##    return 1
##    return 2
##
##print(f())
##
###python don't have concept of call by reference or call by value.
###to emulate this we use mutability.
###Mutable Type->CALL BY REFERENCE.
###Non-Mutable Type->CALL BY VALUE.
##
##def changeList(mylist):
##
##    mylist.append([1,2,3])
##    return mylist
##
##mylist=[10,20,30]
##print(mylist)
##changeList(mylist)
##print(mylist)
##
##def changeList(mylist):
##
##    mylist.upper() #string is immutable.
##    return mylist
##
##mylist="psit"
##print(mylist)
##changeList(mylist)
##print(mylist)
##
##def changeList(mylist):
## 
##    return mylist.upper()
##
##mylist="psit"
##print(mylist)
##changeList(mylist)
##print(mylist)
##
###keyword argument:-
##
##def printinfo(name,age):
##
##    print("Name:",name)
##    print("age:",age)
##
##printinfo(50,"nikki")
##printinfo(age=50,name="nikki") #keyword argument don't need to remember the order in which arguments are passed.


#default value argument:-
##
##def printinfo(name,age=30): #default value argument.
##                            #if no value during function call is passed then it will take its default value.                
##    print("Name:",name)
##    print("age:",age)
##
##printinfo(age=50,name="nikki")
##printinfo("mikki")
##print(printinfo.__doc__)

#Variable length Arguments:-

##def demo(x,y,*z): #all variable remaining will be assigned as a tuple to *z.
##
##    print(x,y,z)
##
##demo(2,3,20,30)
##demo(2,3,1,2,3,4,5)
##demo(2,3)

##def f5(x,y=6,*z): #all variable remaining will be assigned as a tuple to *z.
##
##    print(x,y,z)
##
##f5(2,3,4,5,6)
##f5(12)

#variable no of dictionery elements passed.

##def f1(x,y,**z):
##
##    print(x,y,z)
##
##f1(2,3,psit=25,b=67,c=89,d=4) #"psit=25,b=67,c=89,d=4" assigned to **z as dictionery.
##f1(12,14)

##def f1(*args,**kwargs):
##
##    print(args,kwargs)
##
##f1(2,3,a=3,b=4,c=7)

##def f1(a,b,*args,**kwargs):
##
##    print(a,b,args,kwargs)
##
##f1(0,1,4,5,2,3,d=3,e=4,f=7)

##def f1(**kwargs,*args): #syntax error.
##
##    print(args,kwargs)
##
##f1(a=3,b=4,c=7,0,1,4,5,2,3)

#returning multiple values
#python function can return multiple values.

##def calc(a,b):
##
##    return a+b,a-b,a*b,a**b
##
##print(calc(2,3))

#there is no concept of function overloading in python.
#function having multiple same names only last definition  is considered the previous are ignored.

##def fun(a,b):
##    print(a+b)
##
##def fun(a,b,c):
##    print(a+b+c)
##
##def fun(a,b,c,d): #function overloading only last definitioni is considered.
##    print(a+b+c+d)
##
##fun(2,3,4,5)

#in python function are also an object the def statement creates an object and binds it to name.to call it we use.

def message():

    return "hello"

print(message) #gives object address.
print(message())

fun=message #creates object of name fun pointing to message.
print(fun())




