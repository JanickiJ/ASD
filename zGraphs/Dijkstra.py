from queue import PriorityQueue


def dijkstra(G,s):
    n=len(G)
    parent = [None]*n
    distance = [float('inf')]*n

    q= PriorityQueue()
    distance[s] = 0
    q.put((distance[s],s,0))

    while not q.empty():
        x = q.get()
        dis = x[0]
        u = x[1]
        prev = x[2]
        for v in range(n):
            if G[u][v] > 0 and G[u][v] != prev:
                if distance[v] > distance[u] + G[u][v]:
                    distance[v] = distance[u] + G[u][v]
                    parent[v] = u
                    q.put((distance[v], v, G[u][v]))
    return distance
G=[[(1,1),(2,2)],[(0,1),(3,4)],[(0,2),(3,2)],[(1,4),(2,2)]]
print(dijkstra(G,0))

#dijkstra macierz

def dijkstras(G,s):
    n= len(G)
    q= PriorityQueue()

    distance = [float('inf')]*n
    distance[s] = 0

    q.put(distance[s],s)

    while q:
        u=q.get()
        relaxs(G,u[1],distance,q)

def relaxs(G,u,distance,q):
    for v in range(len(G)):
        if G[u][v] is True and distance[v]>distance[u]+G[u][v]:
            q.put()
