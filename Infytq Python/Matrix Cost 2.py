def solution(grid):

    m=len(grid)
    n=len(grid[0])

    for i in range(1,m):

        for j in range(n):

            if j==0:

                grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i-1][j+1])

            elif j==n-1:

                grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i-1][j-1])

            else:

                temp=min(grid[i-1][j],grid[i-1][j-1])

                temp1=min(temp,grid[i-1][j+1])

                grid[i][j]=grid[i][j]+temp1

    mincost=grid[m-1][0]

    for i in grid[m-1]:

        if i%2==1:

            if i<mincost:

                mincost=i

    if mincost%2!=1:

        return -1

    return mincost


grid=[[1,5,2],[7,2,2],[2,8,1]]

print(solution(grid))
