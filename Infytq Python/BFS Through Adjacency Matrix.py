graph = [
          [0, 1, 1, 0, 0],
          [0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0],
          [1, 0, 0, 0, 1],
          [0, 0, 0, 0, 0]
]

def BFS(source):

    queue.append(source)
    visited.append(source)

    while queue:

        current=queue.pop(0)

        for j in range(n):

            if j not in visited and graph[current][j]==1:

                visited.append(j)
                queue.append(j)

    return visited

n=len(graph)
queue=[]
visited=[]

print(BFS(0))
