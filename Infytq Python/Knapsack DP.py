n=3
w=4

values=[1,2,3]
weight=[4,5,1]

def knapsack(weight,values,w,n):

    col=w+1
    row=len(values)+1

    dp=[[0]*col for i in range(row)]

    for i in range(row):

        for j in range(col):

            if weight[i-1]>j:

                dp[i][j]=dp[i-1][j]

            else:

                dp[i][j]=max(values[i-1]+dp[i-1][j-weight[i-1]],dp[i-1][j])

    return dp[-1][-1]

res=knapsack(weight,values,w,n)

print(res)

