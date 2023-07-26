import math

N,S,M=map(int,input().split())

if ((N*6)<(M*7) and s>6) or N<M:

    print("NO")

else:

    days=math.ciel((S*M)/N)

print(days)
