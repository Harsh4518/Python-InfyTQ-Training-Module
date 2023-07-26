arr=[2,1,2]

d={}

for i in arr:

    d[i]=d.get(i,0)+1

total=0

for i in d.keys():

    if d[i]>1:

        total+=d[i]-1

print(total)

        
