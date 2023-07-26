isconnected=[[1,1,0],[1,1,0],[0,0,1]]

def DFS(source):

    global c
    
    visited.append(source)

    for i in range(n):

        if i not in visited:

            DFS(i)
            c+=1

    return c

n=len(isconnected)
visited=[]
c=0

print(DFS(0))

