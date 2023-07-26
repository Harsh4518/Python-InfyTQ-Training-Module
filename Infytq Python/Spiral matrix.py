matrix=[[25,1,29,7],[24,20,4,32],[16,38,29,1],[48,25,21,19]]

def spiral(i,j,m,n):

    if i>=m and j>=n:

        return 

    for x in range(i,m):

        print(matrix[x][j],end=" ")

    for x in range(j+1,n):

        print(matrix[m-1][x],end=" ")

    if n-1!=j:

        for x in range(m-2,i-1,-1):

            print(matrix[x][n-1],end=" ")

    if m-1!=i:

        for x in range(n-2,j,-1):

            print(matrix[i][x],end=" ")

    spiral(i+1,j+1,m-1,n-1)

spiral(0,0,len(matrix),len(matrix[0]))
