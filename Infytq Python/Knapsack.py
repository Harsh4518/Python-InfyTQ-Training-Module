n=3
w=4

values=[1,2,3]
weight=[4,5,1]

def knapsack(weight,values,w,n):

    if w==0 or n==0:

        return 0

    elif weight[n-1]>w:

        return knapsack(weight,values,w,n-1)

    else:

        return max(values[n-1]+knapsack(weight,values,w-weight[n-1],n-1),knapsack(weight,values,w,n-1))

res=knapsack(weight,values,w,n)

print(res)

