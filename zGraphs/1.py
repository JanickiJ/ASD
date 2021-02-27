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


def BFS(arr,s):
    n = len(arr)
    q = Queue()
    visited = [False]*n
    parent = [None]*n

    q.enqueue(s)
    visited[s] = True
    parent[s] = (None,0)

    while not q.is_empty():
        q.print()
        u = q.dequeue()
        for v in range(n):
            if arr[u][v] == 1 and not visited[v]:
                visited[v] = True
                parent[v] = (v,parent[u][1]+1)
                q.enqueue(v)
    return parent
G = [[0,1,0,0],[0,0,1,0],[0,0,0,1], [0,0,0,0]]
print( BFS(G,0) )


