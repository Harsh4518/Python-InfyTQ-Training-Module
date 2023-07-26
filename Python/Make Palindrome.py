l=[1,4,5,9,1]
c=0

i=0
j=len(l)-1

while i<=j:

    if l[i]==l[j]:

        i+=1
        j-=1

    elif l[i]<l[j]:

        i+=1
        l[i]+=l[i-1]
        c+=1
        

    elif l[i]>l[j]:

        j-=1
        l[j]+=l[j+1]
        c+=1
        

print(c)
