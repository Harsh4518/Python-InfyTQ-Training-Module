grid=[['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]

def dfs(i,j):

    if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1 or (i,j) not in visited:

        return

    visited.add(i,j)

    dfs(i+1,j)
    dfs(i-1,j)
    dfs(i,j+1)
    dfs(i,j-1)

m=len(grid)
n=len(grid[0])
visited=set()
count=0

for i in range(m):

    for j in range(n):

        if (i,j) not in visited and grid[i][j]=='1':

            dfs(i,j)
            count+=1

print(count)

        
