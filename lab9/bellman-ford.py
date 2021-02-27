def bellman_ford(G, s):
    n = len(G)
    parent = [None] * n
    distance = [float('inf')] * n

    distance[s] = 0

    for _ in range(n - 1):
        for u in range(n):
            for i in range(len(G[u])):
                v = G[u][i][0]
                if distance[v] > distance[u] + G[u][i][1]:
                    distance[v] = distance[u] + G[u][i][1]
                    parent[v] = u

    for u in range(n):
        for v in range(len(G[u])):
            if distance[v] > distance[u] + G[u][v][1]:
                print("Cykl ujemny")
                return
    return distance


G = [[(1, 2)], [(2, 1)], [(3, 3)], [(4, -1), (5, 6)], [(1, 2)], []]
print(bellman_ford(G, 0))

G = [[0, 2, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 3, 0, 0, 0],
     [0, 0, 0, 0, -1, 6, 0],
     [0, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]
     ]


def belmanfordmatrix(G, s):
    n = len(G)
    dist = [float('inf')] * n
    par = [None] * n
    dist[s] = 0
    for t in range(n - 1):
        for u in range(n):
            for v in range(n):
                if G[u][v] != 0 and dist[v] > dist[u] + G[u][v]:
                    par[v] = u
                    dist[v] = dist[u] + G[u][v]
    for u in range(n):
        for v in range(n):
            if G[u][v]!=0 and dist[v] > dist[u] + G[u][v]:
                print("Cykl ujemny")
                return
    return dist


Gr = [[0, 2, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 3, 0, 0, 0],
      [0, 0, 0, 0, -1, 6, 0],
      [0, 2, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0]
      ]
print(belmanfordmatrix(Gr, 0))
