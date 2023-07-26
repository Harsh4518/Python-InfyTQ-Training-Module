a=7
b=9

l=[]
flag=1

for i in range(a,b+1):

    for x in range(2,int(i**0.5)+1):

        if i%x==0:
            
            break

    else:

        l.append(i)

print(max(l)-min(l))

        
    
