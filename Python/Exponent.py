def expo(x,y):

    res,i=1,1

    while i<=y:

        res=res*x
        i+=1

    return res

ans=expo(3,4)
print(ans)

n=int(input("Enter a number:"))
p=2

while n!=0:

    for i in range(2,p):

        if p%i==0:
            break

    else:
        print(p)
        n-=1
    
    p+=1



