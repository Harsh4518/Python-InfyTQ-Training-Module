arr=[9,10,2,6,7,12,8,1]
res=0

for i in range(len(arr)):

    for j in range(i+1,len(arr)):

        if arr[j]>arr[i]:

            t=j-i

            res=max(t,res)

print(res)
