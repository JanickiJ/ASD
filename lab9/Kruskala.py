class Vertex:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0


class Graph:
    def __init__(self,n):
        self.edges = []
        self.vertices = [None]*n

    def addEdge(self, u, v, weight):
        if self.vertices[u] is None:
            self.vertices[u] = Vertex(u)
        if self.vertices[v] is None:
            self.vertices[v] = Vertex(v)

        self.edges.append([u, v, weight])


def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


# tablica krawedzi (x,y,waga)

def printresult(A):
    for i in range(len(A)):
        print(A[i][0],A[i][1])

def kruskal(graph):
    n = len(graph.edges)
    graph.edges = sorted(graph.edges, key=lambda item: item[2])

    A = []

    for i in range(n):
        u = graph.edges[i][0]
        v = graph.edges[i][1]

        if find_set(graph.vertices[u]).id != find_set(graph.vertices[v]).id:
            A.append((u, v))
            union(graph.vertices[u], graph.vertices[v])

    return A


g = Graph(9)
g.addEdge(0, 1, 2)
g.addEdge(0, 6, 1)
g.addEdge(0, 5, 6)
g.addEdge(1, 2, 3)
g.addEdge(2, 6, 2)
g.addEdge(2, 3, 1)
g.addEdge(3, 4, 7)
g.addEdge(4, 5, 8)
g.addEdge(4, 6, 5)
printresult(kruskal(g))

T=[(1,10),(2,8),(1,8),(5,8),(1,1),(10,2)]
T = sorted(T)
print(T)