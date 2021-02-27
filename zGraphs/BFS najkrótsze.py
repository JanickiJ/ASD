class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def put(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def get(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
    def print(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next
    def empty(self):
        return self.head is None


def BFSsciezki(G, s, t):
    q = Queue()
    n = len(G)
    visited = [False] * n
    parent = [None] * n

    q.put((s, 0, None))
    while not q.empty() and not visited[t]:
        x = q.get()
        u = x[0]
        if x[1] > 0:
            q.put((u, x[1] - 1, x[2]))
        else:
            if not visited[u]:
                visited[u] = True
                parent[u] = x[2]
                for i in range(len(G[u])):
                    v = G[u][i][0]
                    waga = G[u][i][1]
                    if not visited[v]:
                        q.put((v, waga-1, u))
    result = []
    par = t
    while par != s:
        par = parent[par]
        result.append(par)
    print(result)


G = [[(1, 2), (4, 6)], [(0, 2), (2, 2),(3,2), (4, 2)], [(1, 2), (3, 5)], [(1,2),(2, 5), (4, 1)], [(0, 6), (3, 1)]]

BFSsciezki(G,0,3)

