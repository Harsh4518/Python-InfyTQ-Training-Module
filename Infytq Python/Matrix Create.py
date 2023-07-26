r,c=2,3

matrix=[[0]*(c)]*(r)

l=[i for i in range(1,(r*c)+1)]
print(l)
index=0

for i in range(r):

    for j in range(c):

        matrix[i][j]=l[index]
        print(matrix)
        index+=1

print(matrix)