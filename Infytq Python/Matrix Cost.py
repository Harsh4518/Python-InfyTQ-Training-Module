matrix=[[1,3,1],[1,5,1],[4,2,1]]
m=len(matrix)
n=len(matrix[0])

def solution(matrix,m,n):

    if m==0 and n==0:

        return matrix[m][n]

    elif m<0 or n<0:

        return float('inf')

    else:

        return min(matrix[m][n]+solution(matrix,m-1,n), matrix[m][n]+solution(matrix,m,n-1))

s=solution(matrix,m-1,n-1)

print(s)
        
