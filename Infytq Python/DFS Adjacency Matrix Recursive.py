mat = [
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]
]

def DFS(source):

    visited.append(source)

    for i in range(n):

        if i not in visited and mat[source][i]==1:

            DFS(i)

    return visited

n=len(mat)
visited=[]
print(DFS(0))




