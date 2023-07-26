mat=[[0,1,1,0,0],[0,0,0,1,1],[0,0,0,1,0],[1,0,0,0,1],[0,0,0,0,0]]

n=len(mat)

graph={}

for i in range(n):

    for j in range(n):

        if i not in graph:

            graph[i]=[]

        if j not in graph:

            graph[j]=[]


        if mat[i][j]==1 and i!=j:

            graph[i].append(j)

print(graph)
