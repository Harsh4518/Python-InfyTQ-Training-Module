def fallingpath(i,j,mat):

    if j<0 or j>n-1:

        return float('inf')

    if i==0:
        
        return mat[0][j]

    else:

        u=mat[i][j]+fallingpath(i-1,j,mat)
        ld=mat[i][j]+fallingpath(i-1,j-1,mat)
        rd=mat[i][j]+fallingpath(i-1,j+1,mat)

        return min(u,ld,rd)

matrix=[[2,1,3],[6,5,4],[7,8,9]]
m=len(matrix)
n=len(matrix[0])

arr=[]

for j in range(n):

    result=fallingpath(m-1,j,matrix)
    arr.append(result)

print(min(arr))
    
