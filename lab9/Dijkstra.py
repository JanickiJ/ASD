from queue import PriorityQueue

def relax(G,u,distance,parent,q):
    for i in range(len(G[u])):
        v = G[u][i][0]
        if distance[v] > distance[u] + G[u][i][1]:
            distance[v] = distance[u] + G[u][i][1]
            parent[v] = u
            q.put((distance[v],v))

def dijkstra(G,s):
    n=len(G)
    parent = [None]*n
    distance = [float('inf')]*n

    q= PriorityQueue()
    distance[s] = 0
    q.put((distance[s],s))

    while not q.empty():
        u = q.get()
        relax(G,u[1],distance,parent,q)

    return distance
G=[[(1,1),(2,2)],[(0,1),(3,4)],[(0,2),(3,2)],[(1,4),(2,2)]]
print(dijkstra(G,0))

