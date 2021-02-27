# Jakub Janicki
# Odpalam algorytm dijkstry z modyfikacja
# w kolejce priorytetowej bede przechowywał krotki (distans do s, s, srodek transportu ktorym docieramy do s)
# dokładam modyfikacje tak aby nie wychodzic z wierzchołka tym samym srodkiem transportu co wchodziłem
# O(ElogV)

from zad1testy import runtests


class PriorityQueue:
    def __init__(self):
        self.Q = [None] * 10000
        self.tail = -1
        self.head = 0
        self.size = 0

    def put(self, krotka):
        self.tail += 1
        self.size += 1
        self.Q[self.tail] = krotka

        i = self.tail
        while i > self.head and krotka[0] < self.Q[i - 1][0]:
            self.Q[i] = self.Q[i - 1]
            i -= 1

        self.Q[i] = krotka

    def get(self):
        krotka = self.Q[self.head]
        self.size -= 1
        self.head += 1

        return krotka

    def empty(self):
        if self.size == 0:
            return True
        else:
            return False


def islands(G, A, B):
    n = len(G)
    parent = [None] * n
    distance = [float('inf')] * n

    q = PriorityQueue()
    distance[A] = 0
    q.put((distance[A], A, 0))

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

    result = distance[B]
    if result != float('inf'):
        return result
    else:
        return None
    pass


runtests(islands)
