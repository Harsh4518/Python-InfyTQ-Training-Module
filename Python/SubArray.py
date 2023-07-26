a=[6,-4,-3,2,3]

x=sum(a)/2
s=0

for i in range(len(a)-1):

    s+=a[i]

    if s==x:

        index=i
        break


print(a[0:i+1],a[i+1:])
