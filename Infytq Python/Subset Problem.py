arr=[1,3,4,5]
n=4
k=7

def subset(arr,k,n):

    col=k+1
    row=len(arr)+1

    dp=[[False]*col for i in range(row)]

    for i in range(1,row):

        dp[i][0]=False

    for i in range(col):

        dp[0][i]=True

    for i in range(1,row):

        for j in range(1,col):

            if arr[i-1]>j:

                dp[i][j]=dp[i-1][j]

            else:

                dp[i][j]=(dp[i-1][j-arr[i-1]] or dp[i-1][j])

    return dp[-1][-1]

res=subset(arr,k,n)

print(res)

