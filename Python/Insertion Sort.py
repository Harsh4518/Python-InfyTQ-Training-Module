#INSERTION SORT
#Complexity:O(n**2) (Worst Case)
#Complexity:O(n) (Best Case)

l=[1,5,4,3,2,9,0]

"""for i in range(len(l)):

    pos=i

    while pos>0 and l[pos]<l[pos-1]:

        l[pos],l[pos-1]=l[pos-1],l[pos]
        pos-=1

print(l)"""

#T(n)=(n-1)+T(n-1),T(1)=1

#Recurrance Relation.

def insertion(l,s,n):

    if s>=n:

        return

    p=s

    while p>0 and l[p]<l[p-1]:

        l[p],l[p-1]=l[p-1],l[p]
        p=p-1

    insertion(l,s+1,n)

    return l

print(insertion(l,1,len(l)))
    



        
