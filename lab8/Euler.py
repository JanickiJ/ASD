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
        self.top = N.next
        return N.val
    def is_empty(self):
        return self.top.next is None
    def print(self):
        tmp = Node()
        tmp = self.top.next
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.next




def find_euler_cycle(G,start_node,euler_stack):
    for i in range(len(G)):
        if G[start_node][i]:
            G[start_node][i] = 0
            G[i][start_node] = 0
            find_euler_cycle(G,i,euler_stack)
    euler_stack.append(start_node)

def euler_cycle(G):
    euler_stack = []
    find_euler_cycle(G,0,euler_stack)
    return euler_stack

G=[
    [0,1,1,1,1],
    [1,0,1,0,0],
    [1,1,0,0,0],
    [1,0,0,0,1],
    [1,0,0,1,0]
]
s = euler_cycle(G)
print(s)
