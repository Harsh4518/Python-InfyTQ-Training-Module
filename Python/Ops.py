ops="52CD+"

res=[]

for i in range(len(ops)):

    if isinstance(ops[i],int)==0:

        res.append(ops[i])

    if ops[i]=='C':

        res.pop()

    if ops[i]=='D':

        t=res[-1]
        res.append(2*t)

    if ops[i]=="+":

        x1=res[-1]
        x2=res[-2]
        res.append(x1+x2)
        




    

