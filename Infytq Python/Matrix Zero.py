matrix=[[1,1,0,1,1],[1,1,1,1,1],[1,1,1,0,1],[1,1,1,1,1],[0,1,1,1,1]]

col=[False]*len(matrix[0])
row=[False]*len(matrix)

for i in range(len(matrix)):

    for j in range(len(matrix[0])):

        if matrix[i][j]==0:

            col[j]=True
            row[i]=True

for i in range(len(matrix)):

    if row[i]==True:

        for j in range(len(matrix[0])):

            matrix[i][j]=0

for j in range(len(matrix[0])):

    if col[j]==True:

        for i in range(len(matrix)):

            matrix[i][j]=0

print(matrix)

            
