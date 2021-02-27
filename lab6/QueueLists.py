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


q = Queue()
print(q.is_empty())
q.enqueue(5)
q.enqueue(7)
q.enqueue(12)
q.enqueue(13)
print(q.is_empty())
q.print()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print(q.is_empty())