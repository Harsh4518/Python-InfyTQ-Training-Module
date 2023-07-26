#sin x=x-x^3/3!+x^5/5!-x^7/7!+......n terms
import math
def sine(x,n):

    s=0

    for i in range(1,n):
    
        s=s+(-1)**(i-1)*(x**(2*i-1)/math.factorial(2*i-1))


    print(s)

x,n=list(map(int,input().split()))
x=x*3.14/180.0
sine(x,n)
