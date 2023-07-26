#shallow copy

#whether shallow or deepcopy always a new object is created in shallow copy refernce is passed and in deepcopy no reference is passed.
#whether shallow copy or deep copy is determined by change in nested element.
#Shallow copy nested element both list change.
#deep copy nested element only one list change.

#1.Constructor method (deepcopy)

l1=[1,2,3,4,5]
l2=list(l1) #constructor
#print(id(l1))
#print(id(l2)) 
l1[1]=6
print(l1,l2)


l1=[1,2,3,4,[5,4,6]]  #nested list here shallow copy takes place
l2=list(l1)
l1[4][1]=9
print(l1,l2)

l1=[1,2,3,4,[5,6,7]]
l2=list(l1)
l1.append(10) #deep copy
print(l1,l2)

l1=[1,2,3,4,[5,6,7]]
l1.append(10)
l2=list(l1) #shallow copy
print(l1,l2)

#2.Copy() Method

l1=[1,2,3,4,[5,6,7]]
l2=l1.copy() #deep copy
l1[1]=9
print(l1,l2)

#3.Copy Module
import copy
l1=[1,2,3,4,[5,6,7]]
l2=copy.copy(l1)
l1[1]=0
print(l1,l2)

#Nested  elements are manipulated then shallow copy takes place both list changes reflect.

l1=[1,2,3,4,[5,6,7]]
l2=l1 #same object reference changes reflect.
l1[2]=9
print(l1,l2)

