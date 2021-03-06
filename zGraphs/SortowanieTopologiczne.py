

def DFSVisit(G,results, visited, u):
    visited[u] = 1
    for v in G[u]:
        if visited[v] == 0:
            DFSVisit(G,results, visited, v)
    results.append(u)

def sortowanieTopologiczne(G):
    n = len(G)
    results = []
    visited = [0] * n
    for u in range(n):
        if visited[u] == 0:
            DFSVisit(G,results, visited ,u)
    results.reverse()
    return results

G = [[],[],[3],[1],[0,1],[0,2]]
print( sortowanieTopologiczne(G) )
