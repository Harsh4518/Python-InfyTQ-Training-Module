matrix=[[1,3,1],[1,5,1],[4,2,1]]
m=len(matrix)
n=len(matrix[0])

def solution(matrix):

    for i in range(m):

        for j in range(n):

            if i==0 and j==0:

                continue

            else:

                if i>0:

                    t=matrix[i][j]+matrix[i-1][j]

                else:

                    t=matrix[i][j]+float('inf')

                if j>0:

                    l=matrix[i][j]+matrix[i][j-1]

                else:

                    l=matrix[i][j]+float('inf')

                matrix[i][j]=min(t,l)

    return matrix[-1][-1]

print(solution(matrix))

            
