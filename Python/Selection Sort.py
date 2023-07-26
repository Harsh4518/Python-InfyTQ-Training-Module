#SELECTION SORT
#Recurrance Relation: T(n)=n+(n+1)+(n+2)+...........+2+1=n(n+1)/2=O(n**2)

a=[3,6,4,8,5,1,0]

#iterative method
"""for i in range(len(a)):

    m=i

    for j in range(i+1,len(a)):

        if a[j]<a[m]:

            m=j

    a[i],a[m]=a[m],a[i]

print(a)"""

#recursive method
#Recurrance Relation: T(n)=n+T(n-1)

def selection(A,start,n):

    if start>=n-1:

        return

    m=start

    for i in range(start+1,n):

        if a[i]<a[m]:

            m=i

    a[start],a[m]=a[m],a[start]
    selection(a,start+1,n)

selection(a,0,len(a))
print(a)



        
