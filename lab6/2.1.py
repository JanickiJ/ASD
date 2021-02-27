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

def BFSdwudzielny(arr):

    if arr is None:
        return False

    n = len(arr)
    queue = Queue()
    color=[0]*(len(arr))
    color[0] = 1
    print(color)
    queue.enqueue(0)

    while not queue.is_empty():
        parent = queue.dequeue()
        for v in arr[parent]:
            print(parent, v)
            if color[v] == color[parent]:
                return False
            elif color[v] == 0:
                if color[parent] == 1:
                    color[v] = 2
                else:
                    color[v] = 1
                queue.enqueue(v)
    return True

G = [[3],[2,3,4],[4],[1,0],[1,2]]
print(BFSdwudzielny(G))