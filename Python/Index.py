a=[5,5,5,5,2]

c=0

for i in range(len(a)):

    t=i+1
    r=a[i]

    if (r-1)>len(a):

        continue

    else:

        if a[r-1]==t:

print(c)
