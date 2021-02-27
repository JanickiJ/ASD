import queue


def BFSdwudzielny(arr):
    n = len(arr)
    q = queue.Queue()
    color = [0] * (len(arr))
    color[0] = 1
    q.put(0)

    while not q.empty():
        parent = q.get()
        for v in arr[parent]:
            if color[v] == color[parent]:
                return False
            elif color[v] == 0:
                if color[parent] == 1:
                    color[v] = 2
                else:
                    color[v] = 1
                q.put(v)
    return color

def BFS(G, s, t, parent):
    n = len(G)
    visited = [False] * n

    q = queue.Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()

        for v in range(n):
            if not visited[v] and G[u][v] > 0:
                parent[v] = u
                visited[v] = True
                q.put(v)
    print(visited[t])
    return visited[t]


def ford_fulkerson(G, s, t):
    n = len(G)
    parent = [None] * n
    max_flow = 0
    while BFS(G, s, t, parent):
        min_flow = float('inf')
        v = t

        while v != s:
            u = parent[v]
            min_flow = min(min_flow, G[u][v])
            v = u

        max_flow += min_flow
        v = t
        while v != s:
            u = parent[v]
            G[u][v] -= min_flow
            G[v][u] += min_flow
            v = u
    return max_flow

def skojarzenia(G):
    color = BFSdwudzielny(G)
    n = len(G)
    arr = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

    for i in range(1, n + 1):
        if color[i - 1] == 1:
            arr[0][i] = 1
        if color[i - 1] == 2:
            arr[i][n + 1] = 1

    for u in range(len(G)):
        if color[u] == 1:
            for v in G[u]:
                arr[u+1][v+1] = 1

    return ford_fulkerson(arr, 0, n+1)

G = [[3,4], [5], [4], [1], [0,2], [1]]
print(skojarzenia(G))
