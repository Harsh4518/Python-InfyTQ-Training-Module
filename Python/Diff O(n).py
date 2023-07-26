arr=[9,10,2,6,7,12,8,1]
n=len(arr)

l=[0]*len(arr)
R=[0]*len(arr)

l[0]=arr[0]

for i in range(1,len(arr)-1):

    l[i]=min(arr[i],l[i-1])

R[len(R)-1]=arr[len(arr)-1]

for i in range(len(arr)-2,-1,-1):

    R[i]=max(arr[i],R[i+1])

i,j=0,0
res=0

while i<n and j<n:

    if l[i]<=R[j]:

        res=max(res,j-i)
        j+=1

    else:

        i+=1

print(res)
