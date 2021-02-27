class Queue:
    def __init__(self, n):
        self.size = 0
        self.head = 0
        self.arr=[None]*n
    def enqueue(self, val):
        self.arr[(self.head + self.size) % len(self.arr)] = val
        self.size += 1

    def is_full(self):
        return self.size == len(self.arr)

    def dequeue(self):
        result = self.arr[self.head]
        self.arr[self.head] = None
        self.head = (self.head +1) % len(self.arr)
        self.size -= 1
        return result
    def print(self):
        for i in range(self.size):
            print(self.arr[(self.head+i)%len(self.arr)])
q=Queue(10)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(8)
q.enqueue(8)
q.dequeue()
q.dequeue()
q.enqueue(8)
q.enqueue(8)
q.enqueue(8)
q.enqueue(8)
q.enqueue(8)
print(q.arr)
print(q.is_full())
q.enqueue(8)
print(q.is_full())