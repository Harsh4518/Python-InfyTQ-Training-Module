def triangle(matrix):
    
    n=len(matrix[-1])

    dp=[[0]*n for i in range(n)]

    for j in range(n):

        dp[n-1][j]=matrix[n-1][j]
        
    for i in range(n-2,-1,-1):

        for j in range(i,-1,-1):

            down=matrix[i][j]+dp[i+1][j]
            diag=matrix[i][j]+dp[i+1][j+1]
            dp[i][j]=min(down,diag)

    return dp[0][0]

mat=[[2],[3,4],[6,5,7],[4,1,8,3]]

print(triangle(mat))
