l=[-3,-2,2,3]

l.sort()

for i in l:

    if i>0:

        temp=i
        break
else:

    print("1")

try:
    temp2=max(l)+1

    s=0

    for i in range(temp-1,temp2+1):

        if i not in l and i!=0:

            print(i)
            break
except:

    pass

