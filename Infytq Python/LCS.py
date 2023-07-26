s1="abcde"
s2="ace"

def lcs(s1,s2,m,n):

    dp=[[-1]*(n+1) for i in range(m+1)]

    for i in range(m+1):

        for j in range(n+1):

            if i==0 or j==0:

                dp[i][j]=0

            if s1[i-1]==s2[j-1]:

                dp[i][j]=dp[i-1][j-1]+1

            else:

                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    return dp[-1][-1]

m=len(s1)
n=len(s2)

res=lcs(s1,s2,m,n)

print(res)
