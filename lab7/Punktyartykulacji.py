# dfs z czasem
def mosty(G):
    n = len(G)
    visited = [False] * n
    entry = [-1] * n
    low = [None] * n
    parent = [None] * n

    for u in range(len(G)):
        if not visited[u]:
            DFSvisittime(G, u, parent, visited, entry, low)

    for i in range(len(G)):
        print(entry[i],(low[i]))
        if entry[i] <= low[i] and parent[i] is not None:
            print(i)


t = 0


def DFSvisittime(G, u, parent, visited, entry, low):
    global t
    t += 1
    visited[u] = True
    entry[u] = t
    low[u] = t
    for v in range(len(G)):
        if G[u][v]:
            G[u][v] = 0
            G[v][u] = 0
            if visited[v]:
                low[u] = min(low[v], low[u])
            else:
                parent[v] = u
                DFSvisittime(G, v, parent, visited, entry, low)

    if parent[u] is not None:
        low[parent[u]] = min(low[parent[u]], low[u])


G = [
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

mosty(G)
