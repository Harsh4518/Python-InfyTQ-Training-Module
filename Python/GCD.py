x=18
y=24

while x!=0:

    x,y=y%x,x
    """t=x
       x=y%x
       y=t"""

print(y)

def GCD(x,y):

    if x==0:

        return y

    else:

        return GCD(y%x,x)

print(GCD(18,24))


