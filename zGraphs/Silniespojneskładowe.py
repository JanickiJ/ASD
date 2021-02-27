def DFStime(G, visited, entry, process):
    for u in range(len(G)):
        if not visited[u]:
            DFSvisittime(G, u, visited, entry, process)


t = 0


def DFSvisittime(G, u, visited, entry, process):
    global t
    t+=1
    visited[u] = True
    entry[u] = t

    for v in range(len(G)):
        if G[u][v] and not visited[v]:
            DFSvisittime(G, v, visited, entry, process)

    t += 1
    process[u] = t


def DFS(G, visited, process, result):
    max_u = -1
    max_time = -1

    while not min(visited):
        max_time = -1
        for u in range(len(G)):
            if process[u] > max_time and not visited[u]:
                max_u = u
                max_time = process[u]


        DFSvisit(G, max_u, visited, result)
        result.append(-1)




def DFSvisit(G, u, visited, result):
    visited[u] = True
    result.append(u)

    for v in range(len(G)):
        if G[u][v] and not visited[v]:
            DFSvisit(G, v, visited, result)



def silniespojneskladowe(G):
    n = len(G)
    visited = [False] * n
    entry = [0] * n
    process = [0] * n
    result = []
    DFStime(G, visited, entry, process)
    for i in range(n):
        visited[i] = False
        for j in range(n):
            if G[i][j] == 1:
                G[i][j] = 0
                G[j][i] = 2

    DFS(G, visited, entry, result)
    print(result)


G = [
    [0, 1, 0, 0, 0, 0,0],
    [0, 0, 1, 1, 0, 0,0],
    [0, 0, 0, 0, 1, 0,0],
    [1, 0, 0, 0, 0, 0,1],
    [0, 0, 0, 0, 0, 1,0],
    [0, 0, 1, 0, 0, 0,0],
    [1, 0, 0, 0, 0, 0,0]
]

silniespojneskladowe(G)
