x=0
y=0

n=int(input("Enter the no of commands:"))

for i in range(n):

    movement,value=map(str,input().split())

    if movement=="UP":

        y+=int(value)

    elif movement=="DOWN":

        y-=int(value)

    elif movement=="LEFT":

        x-=int(value)

    else:

        x+=int(value)

dist=int((x**2+y**2)**0.5)
print(dist)

    

    

