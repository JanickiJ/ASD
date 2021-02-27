#będę uzywał kolejki, dlatego impementuje ja uzywajac do tego 2 stosow

class Node:
    def __init__(self):
        self.val = None
        self.next = None


class Stack:
    def __init__(self):
        self.top = Node()

    def push(self, val):
        new = Node()
        new.val = val
        new.next = self.top.next
        self.top.next = new

    def pop(self):
        N = self.top.next
        self.top.next = N.next
        return N.val

    def is_empty(self):
        return self.top.next is None

    def print(self):
        tmp = self.top.next
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.next


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def is_empty(self):
        return self.stack1.is_empty()

    def enqueue(self, val):
        self.stack1.push(val)

    def dequeue(self):
        if self.stack2.is_empty():
            if self.stack1.is_empty():
                return
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def print(self):
        self.stack2.print()
        self.stack1.print()

# G to macierz opisująca graf: G[i][j]==1 jeśli jest
# wierzchołek z i do j. W przeciwnym razie G[i][j]=0
# s to numer wierzchołka źródłowego
# tu proszę umieścić swoją implementację

#tworze tablice results ktora bedzie moja listą wynikowa
#zarazem bedzie zawierac informacje czy wierzchołek był odwiedzony oraz o odległosci od poczatku jego rodzica
def BFS( G, s ):
    n = len(G)
    results = [None]*n
    #jesli nie ma połaczenia w z wierzchołkiem to wypisze None
    if n == 0:
        return results

    queue = Queue()
    queue.enqueue(s)
    results[s] = (None, 0)
    while not queue.is_empty():
        parent = queue.dequeue()
        for i in range(n):
            if G[parent][i] == 1 and results[i] is None:
                results[i] = (parent, results[parent][1]+1)
                queue.enqueue(i)
    return results

# elementarny test, powinien wypisać
# [(None,0), (0,1), (0,1), (2,2)]
# lub
# [(None,0), (0,1), (0,1), (1,2)]
G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
print( BFS(G,0) )
