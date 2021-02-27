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

stack= Stack()
stack.push(5)
stack.push(10)
print(stack.pop())
stack.push(12)
stack.push(13)
stack.push(2)
stack.push(1)
stack.print()
print(stack.pop())
print(stack.pop())