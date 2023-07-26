def lis(arr):

    n=len(arr)
    dp=[1]*n

    for i in range(1,n):

        for j in range(i):

            if arr[j]<arr[i]:

                dp[i]=max(1+dp[j],dp[i])

    return max(dp)

nums=[7,7,7,7,7,7,7,7]
print(lis(nums)) 



