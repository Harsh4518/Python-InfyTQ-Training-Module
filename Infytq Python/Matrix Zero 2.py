matrix=[[1,1,0,1,1],[1,1,1,1,1],[1,1,1,0,1],[1,1,1,1,1],[0,1,1,1,1]]

m,n=len(matrix),len(matrix[0])
row=col=False

for j in range(n):

    if matrix[0][j]==0:

        row=True
        break

for i in range(m):

    if matrix[i][0]==0:

        col=True
        break

for  i in range(1,m):

    for j in range(1,n):

        if matrix[i][j]==0:

            matrix[0][j]=matrix[i][0]=0

for  i in range(1,m):

    for j in range(1,n):

        if matrix[0][j]==0 or matrix[i][0]==0:n

            matrix[i][j]=0

i=0

while row and i<n:

    matrix[0][i]=0
    i+=1

i=0

while col and i<m:

    matrix[i][0]=0
    i+=1

print(matrix)












            
