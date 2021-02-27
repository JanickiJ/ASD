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


def BFS(G,s):
    n = len(G)
    visited = [False]*n
    parent = [None]*n

    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u=q.get()

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                visited[v] = True
                q.put(v)
    return parent

def BFS1(G,s):
    n = len(G)
    dis = [0]*n
    par = [None]*n
    visited = [False]*n

    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v]=True
                par[v] = u
                dis[v] = dis[u]+1
                q.put(v)
    return par

G=[[2,1],[0,2],[0,1,3],[2]]
print(BFS1(G,0))