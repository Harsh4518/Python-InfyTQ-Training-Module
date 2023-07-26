def minioperations(x,y,p,q):

    if (y%x)!=0:

        return -1

    d=y//x
    a=0

    while(d%p==0):

        d=d//p
        a+=1

    b=0

    while (d%q==0):

        d=d//q
        b+=1

    if d!=1:

        return -1

    return a+b

x=12
y=2592
p=2
q=3
print(minioperations(x,y,p,q))
