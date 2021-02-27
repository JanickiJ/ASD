#dfs z czasem
def DFStime(G):
    n=len(G)
    visited = [False]*n
    entry = [-1]*n
    process = [-1]*n
    parent = [None]*n

    for u in range(len(G)):
        if not visited[u]:
            DFSvisittime(G, u,parent, visited, entry, process)
    print(parent,visited,entry,process)

t = 0


def DFSvisittime(G, u, parent, visited, entry, process):
    global t
    t+=1
    visited[u] = True
    entry[u] = t

    for v in range(len(G)):
        if G[u][v] and not visited[v]:
            parent[v] = u
            DFSvisittime(G, v,parent, visited, entry, process)

    t += 1
    process[u] = t

#zwykły DFS

def DFSVisit(G,parent, visited, u):
    visited[u] = True
    for v in range(len(G)):
        if G[u][v] == 1 and visited[v] is False:
            parent[v]=u
            DFSVisit(G, parent, visited, v)

def DFS(G):
    n = len(G)
    parent=[None]*n
    visited = [False] * n
    for u in range(n):
        if visited[u] is False:
            DFSVisit(G,parent, visited ,u)

    return parent


G = [
    [0, 1, 0, 0, 0, 0,0],
    [0, 0, 1, 1, 0, 0,0],
    [0, 0, 0, 0, 1, 0,0],
    [1, 0, 0, 0, 0, 0,1],
    [0, 0, 0, 0, 0, 1,0],
    [0, 0, 1, 0, 0, 0,0],
    [1, 0, 0, 0, 0, 0,0]
]

print(DFStime(G))

