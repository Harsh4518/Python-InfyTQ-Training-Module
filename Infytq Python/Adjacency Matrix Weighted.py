nodes,edges=map(int,input("Enter Nodes and Edges:").split())

graph=[[0]*nodes for i in range(nodes)]

v={}
c=0

def add(node1,node2):

    global c

    if node1 not in v:

        v[node1]=c
        c+=1

    if node2 not in v:

        v[node2]=c
        c+=1

    frm=v[node1]
    to=v[node2]
    graph[frm][to]=wt

for i in range(int(edges)):

    node1,node2,wt=input().split()
    add(node1,node2,wt)

print(graph)
    
