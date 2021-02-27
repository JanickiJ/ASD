import queue

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


graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]
print(ford_fulkerson(graph, 0, 5))

