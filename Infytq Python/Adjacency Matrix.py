nodes,edges=map(int,input("Enter Nodes and Edges:").split())

graph=[[0]*nodes for i in range(nodes)]

for i in range(edges):

    frm,to=map(str,input().split())

    try:

        graph[abs(65-ord(frm))][abs(65-ord(to))]=1

    except:

        pass

print(graph)
