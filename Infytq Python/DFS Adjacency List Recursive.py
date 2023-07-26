graph={0: [1, 2], 1: [3, 4], 2: [3], 3: [0, 4], 4: []}
visited=set()
output=[]

def DFS(source):

    visited.add(source)
    output.append(source)

    for i in graph[source]:

        if i not in visited:

            DFS(i)

    return output

print(DFS(0))
