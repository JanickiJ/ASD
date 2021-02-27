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


# G to lista list z informacją o istnieniu krawędzi
# G[i] to lista numerów wierzchołków, które są połączone
# krawędzią z wierzchołkiem i
# tu proszę umieścić swoją implementację
# tablica results bedzie tablica wyjsciowa
# jesli results[i] != None to znaczy ze wierzchołęk i został odwiedzony
def DFSVisit(G, u, results):
    for v in G[u]:
        if results[v] is None:
            results[v] = u
            DFSVisit(G, v, results)

def DFS(G):
    n = len(G)
    results = [None] * n
    for i in range(n):
        if results[i] is None:

            DFSVisit(G, i, results)
    results[0] = None
    return results

# elementarny test. Może wypisać np.
# [None, 0, 1, 2]
G = [[1,2],[0,2,3],[3,1,0],[1,2]]
print( DFS(G) )

