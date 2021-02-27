def dfsvisit(G, u, visited):
    visited[u] = 2
    for v in range(len(G)):
        if G[u][v] == 1:
            print(u, v, visited)
            if visited[v] == 2:
                print(1)
                return True
            elif visited[v] == 0:
                return dfsvisit(G,v,visited)
    visited[u] = 1
    return False


def toposort(G):
    n = len(G)
    visited = [0]* n

    for u in range(n):
        if visited[u] == 0:
            print(dfsvisit(G,u,visited))
            if dfsvisit(G,u,visited):
                return True
    return False

G=[[0,1,0,1],[0,0,1,0],[1,0,0,0],[0,1,0,0]]
print(toposort(G))