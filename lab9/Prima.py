

class PriorityQueue:
    def __init__(self):
        self.q=[]
        self.size = 0
        self.head = 0
        self.tail = -1

    def put(self, v,val ):
        self.size += 1
        self.tail += 1
        self.q.append((v,val))
        i = self.tail-1

        while i >= self.head and self.q[i][1]>val:
            self.q[i+1] = self.q[i]
            i-=1
        self.q[i+1]=(v,val)

    def get(self):
        res = self.q[self.head]
        self.head+=1
        self.size-=1
        return res[0]

    def is_empty(self):
        if self.size==0: return True
        else: return False


def prima(G):
    n=len(G)
    parent=[None]*n
    value = [float("inf")]*n
    visited = [False]*n

    parent[0] = None
    value[0] = 0

    q=PriorityQueue()
    q.put(0,0)

    while not q.is_empty():
        u = q.get()
        if visited[u] is False:
            visited[u] = True
            for i in range(len(G[u])):
                v=G[u][i][0]
                if value[v] > G[u][i][1] and parent[u] != v:
                    value[v] = G[u][i][1]
                    parent[v] = u
                    visited[v] = False
                    q.put(v,value[v])
    print(parent)

#listy sasiedztwa
G=[[(1,2),(2,1),(3,6)], [(0,2),(5,3)], [(0,1),(5,2),(4,5)], [(0,6),(4,8)],[(3,8),(2,5),(6,7)],[(1,3),(2,2),(6,1)],[(4,7),(5,1)]]
prima(G)