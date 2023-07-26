def lcs(s1,s2):

    m=len(s1)
    n=len(s2)

    dp=[['']*(n+1) for i in range(m+1)]

    for i in range(m):

        for j in range(n):

            if i==0 or j==0:

                dp[i][j]=''

            if s1[i]==s2[j]:

                dp[i+1][j+1]=dp[i][j]+s1[i]

            else:

                dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1],key=len)

    return dp[-1][-1]

def scs(str1,str2):

    i,j=0,0
    res=""

    for x in lcs(str1,str2):

        while x!=str1[i]:

            res+=str1[i]
            i+=1

        while x!=str2[j]:

            res+=str2[j]
            j+=1

        res+=x

        i,j=i+1,j+1

    return res+str1[i:]+str2[j:]

s1='abac'
s2='cab'

result=scs(s1,s2)
print(result)
