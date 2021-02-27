class Node:
    def __init__(self):
        self.val = None
        self.next = None


def lenOfList(head):
    counter = 0
    while head is not None:
        head = head.next
        counter += 1
    return counter


def sortSubList(L):
    prev = L
    curr = L.next
    currHead = L

    while currHead.next is not None:
        minPrev = currHead
        curr = currHead.next
        min = curr
        while curr is not None:
            if curr.value < min.value:
                minPrev = prev
                min = curr
            prev = curr
            curr = curr.next
        minPrev.next = min.next
        min.next = currHead.next
        currHead.next = min
        currHead = currHead.next


def printList(L):
    curr = L.next
    while curr is not None:
        print(curr.value)
        curr = curr.next


def linking(b, n):
    L = Node()
    curr = L

    for i in range(n):
        if b[i].next is not None:
            curr.next = b[i].next
            while curr.next is not None:
                curr = curr.next

    return L


def bucketSort(L, k):
    b = [Node() for i in range(k)]

    curr = L.next
    while curr is not None:
        address = curr.next
        curr.next = b[int(k * curr.value / 10)].next
        b[int(k * curr.value / 10)].next = curr
        curr = address

    for i in range(k): sortSubList(b[i])
    for el in b:
        if el.next is not None:
            print(el.next.value)

    return linking(b, k)
    def sortList(head):
    newhead = head

    while newhead.next is not None:
        tmp = newhead.next
        min = newhead.next
        prev_min = newhead
        prev_tmp = newhead
        while tmp is not None:
            if tmp.val < min.val:
                min = tmp
                prev_min = prev_tmp
            prev_tmp = tmp
            tmp = tmp.next
        prev_min.next = min.next
        min.next = newhead.next
        newhead.next = min
        newhead=newhead.next



head=Node()
a=Node()
b=Node()
c=Node()
d=Node()

a.val = 5
b.val = 3
c.val = 3
d.val = 1

head.next=a
a.next = b
b.next = c
c.next = d
d.next = None
bucketsortlist(head,0,6)
printList(head)




