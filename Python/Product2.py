l=[0,1,2,3,4,5]

res=[]

for i in range(len(l)):

    t=l.pop(i)
    product=1

    for j in range(len(l)):

        product=product*l[j]

    res.append(product)

    l.append(t)
    l.sort()

print(res)

        
