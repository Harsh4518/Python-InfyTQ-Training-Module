s="kaak"

l=[]
counter=0

for i in s:

    if l==[] or l[-1]!=i:

        l.append(i)

    else:

        l.pop()
        counter+=1

if counter%2!=0:

    print("A")

else:

    print("B")

    
