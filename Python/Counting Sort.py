def Counting_sort(a,b,k):

    o=[0]*len(a)
    
    for i in a:

        b[i]+=1

    for i in range(1,k+1):

        b[i]=b[i]+b[i-1]

    for j in range(len(a)-1,-1,-1):

        o[b[a[j]]-1]=a[j]
        b[a[j]]=b[a[j]]-1

    print(o)

l=[2,5,3,0,2,3,0,3]
m=max(l)
l2=[0]*(m+1)

Counting_sort(l,l2,m)

