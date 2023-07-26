from collections import Counter
a=[3,1,2,5,3]

A,B=0,0

d=Counter(a)

for i in d.keys():

    if d[i]==2:

        A=i

l=set(a)
s=0

for i in range(1,max(a)+1):

    s=s+i

B=s-sum(l)

print(A,B)

    
