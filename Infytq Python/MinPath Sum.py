def triangle(i,j,matrix):

    n=len(mat[-1])

    if i==n-1:

        return mat[n-1][j]

    else:


        down=matrix[i][j]+triangle(i+1,j,matrix)
        diag=matrix[i][j]+triangle(i+1,j+1,matrix)

        return min(down,diag)

mat=[[2],[3,4],[6,5,7],[4,1,8,3]]
n=len(mat[-1])
i=0
j=0

print(triangle(i,j,mat))
