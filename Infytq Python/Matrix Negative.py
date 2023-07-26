matrix=[[-7,-3,-1,3,5],[-3,-2,2,4,6],[-1,1,3,5,8],[3,4,7,8,9]]

m=len(matrix)
n=len(matrix[0])

count=0
i=0
j=n-1

while i<m-1 and j>=0:

    if matrix[i][j]<0:

        count+=j+1

        i+=1

    else:

        j-=1

print(count)

