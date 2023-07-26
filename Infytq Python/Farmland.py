def DFS(r,c):

    if r<0 or r>=m or c<0 or c>=n or land[r][c]==0:

        return (0,0)

    land[r][c]=0
    r1,c1=DFS(r,c+1)
    r2,c2=DFS(r+1,c)
    hr=max(r1,r2,r)
    hc=max(c1,c2,c)

    return (hr,hc)

land=[[1,0,0],[0,1,1],[0,1,1]]
m=len(land)
n=len(land[0])
ans=[]

for i in range(m):

    for j in range(n):

        if land[i][j]==1:

            x,y=DFS(i,j)

            ans.append([i,j,x,y])

print(ans)
            

            
