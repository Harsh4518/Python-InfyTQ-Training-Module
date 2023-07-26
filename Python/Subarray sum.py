a=[2,3,5,4,5,3,4]

k=[]

n=7

for i in range(len(a)):

    for j in range(i,len(a)):
            
        r=a[i:j+1]

        if r!=[]:

            k.append(r)

for i in k:

    if sum(i)%n==0:

        print(i)

