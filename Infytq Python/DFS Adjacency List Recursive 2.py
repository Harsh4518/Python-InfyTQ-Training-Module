graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D'],
    'D': ['E', 'A'],
    'E': []
}

def DFS(source):

    visited.append(source)

    for neighbour in graph[source]:

        if neighbour not in visited:

            DFS(neighbour)

    return visited

visited=[]
print(DFS('A'))
