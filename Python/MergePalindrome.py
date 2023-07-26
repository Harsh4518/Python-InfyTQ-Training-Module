a=[6,1,3,7]

i=0
j=len(a)-1
c=0

while i<=j:

    if a[i]==a[j]:

        i+=1
        j-=1

    elif a[i]<a[j]:

        a[i]+=a[i+1]
        c+=1
        j-=1
        i+=1
        continue

    elif a[i]>a[j]:

        a[j]+=a[j-1]
        c+=1
        i+=1
        j-=1
        continue

    if a==a[::-1]:

        break

print(c)
