nodes,edges=map(int,input("Enter Nodes and Edges:").split())

graph=[[0]*nodes for i in range(nodes)]

v={}

def add(node1,node2):

    global c

    if node1 not in v:

        v[node1]=[]

    if node2 not in v:
        
        v[node2]=[]

    v[node1].append(node2)

for i in range(int(edges)):

    node1,node2=input().split()
    add(node1,node2)

print(v)
    
