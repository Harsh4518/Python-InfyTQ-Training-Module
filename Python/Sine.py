#S(n)=S(n-1)+(-1)**(n-1)*x**2*n-1/fact(2*n-1) S(1)=x

from math import factorial
def Sine(n,angle):

    if n==1:

        return angle

    else:

        return Sine(n-1,angle)+(-1)**(n-1)*(angle**2*n-1)/factorial(2*n-1)

x=int(input("Enter Angle:"))
x=x*3.14/180.0
print(Sine(50,x))
