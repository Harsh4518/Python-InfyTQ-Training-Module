print("Enter no of elements in set 1:")
    
M=int(input())

l1=[]

print("Enter elements of set 1:")

for i in range(M):
    element=int(input())
    
    l1.append(element)
    
a=set(l1)

print("Enter no of elements in set 1")

N=int(input())

l2=[]

print("Enter elements of set 2")

for i in range(N):
    element=int(input())
    
    l2.append(element)
 
b=set(l2)

c1={}
c2={}
c3={}

c1=a.difference(b)
c2=b.difference(a)

c3=c1.union(c2)

print("Symmetric difference of sets:",c3)
