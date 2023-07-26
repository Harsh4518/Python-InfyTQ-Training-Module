def minicost(arr,revcost):

    n=len(arr)
    dp=[[float('inf')]*2 for i in range(n)]

    dp[0][0]=0
    dp[0][1]=1

    revstr=[i[::-1] for i in arr]

    for i in range(1,n):

        for j in range(2):

            curstr=arr[i] if j==0 else revstr[i]
            curcost=0 if j==0 else revcost[i]

            if curstr>=arr[i-1]:

                dp[i][j]=min(dp[i][j],dp[i-1][0]+curcost)

            if curstr>=revstr[i-1]:

                dp[i][j]=min(dp[i][j],dp[i-1][1]+curcost)

    res=min(dp[n-1][0],dp[n-1][1])

    if res==float('inf'):

        return -1

    else:

        return res

arr=['aa','ba','cc']
revcost=[1,3,1]

print(minicost(arr,revcost))
