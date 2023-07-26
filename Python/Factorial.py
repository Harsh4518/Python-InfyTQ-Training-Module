#n!=n*(n-1)!
#fact(n)=n*fact(n-1) ,fact(0)=1

def fact(n):

    if n==0:

        return 1

    else:

        return n*fact(n-1)

print(fact(5))
