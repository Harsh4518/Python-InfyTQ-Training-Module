graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D'],
    'D': ['E', 'A'],
    'E': []
}

def BFS(source):

    queue.append(source)
    visited.append(source)

    while queue:

        current=queue.pop(0)

        for neighbour in graph[current]:

            if neighbour not in visited:

                visited.append(neighbour)
                queue.append(neighbour)


        return visited

queue=[]
visited=[]

print(BFS('A'))
