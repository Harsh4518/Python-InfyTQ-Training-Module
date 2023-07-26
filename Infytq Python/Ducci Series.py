def next(x):

    n=len(x)

    return [abs(x[i]-x[(i+1)%n]) for i in range(len(x))]

x=[0,653,1854,4063]

num=2

for i in range(num+1):

    x=next(x)

print(x)
