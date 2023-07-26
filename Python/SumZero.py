arr=[6,3,-1,-3,4,-2,2,4,6,-12,-7]

l=[]

for i in range(len(arr)):

    s=0

    for j in range(i,len(arr)):

        s+=arr[j]

        if s==0:

            l.append([i,j])

print(l)
