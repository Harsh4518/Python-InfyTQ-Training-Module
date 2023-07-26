l=[0,1,6]

res=[]

for i in l:

    f=[]

    for j in range(1,i+1):

        if i%j==0:

            f.append(j)

    res.append(sum(f))

print(res)
