a=[1,5,10,20,40,80]
b=[6,7,20,80,100]
c=[3,4,15,20,30,70,80,120]

A=len(a)
B=len(b)
C=len(c)

l=min([A,B,C])
res=[]

for i in range(l):

    if b[i] in a and b[i] in c:

        res.append(b[i])

print(res)
