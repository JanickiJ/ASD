class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.head is None

    def makeFromArray(self, array):
        if len(array) == 0:
            return
        self.head = Node(array[0])
        p = self.head
        self.last = p
        for i in range(1, len(array)):
            q = Node(array[i])
            p.next = q
            p = q
            self.last = p

    def printToConsole(self):
        p = self.first
        while p is not None:
            print(p.val)
            p = p.next

    def hasOneElement(self):
        return self.first == self.last

def MergeSortedList(List1, List2):
    if List1.isEmpty():
        return List2
    result = LinkedList()
    p=Node()
    q=Node()
    r=Node()
    if List1.head.dana < List2.head.dana:
        result.head=List1.head
        r = result.head
        result.last = r
        p=List1.head.next
        q=List2.head
    else:
        result.head=List2.head
        r=result.head
        result.last=r
        p = List2.head.next
        q = List1.head