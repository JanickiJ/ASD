def right(i):
    return i * 2 + 1


def left(i):
    return i * 2


def parent(i):
    return i // 2


def size(A):
    return A[0]


def heapify_min(A, i):
    l = left(i)
    r = right(i)
    min = i
    if l <= size(A) and A[l] < A[min]:
        min = l
    if r <= size(A) and A[r] < A[min]:
        min = r
    if min != i:
        A[i], A[min] = A[min], A[i]
        heapify_min(A, min)


def build_heap_min(A):
    for i in range(size(A) // 2, 0, -1):
        heapify_min(A, i)


def heapify_max(A,i):
    l = left(i)
    r = right(i)
    max = i
    if l <= size(A) and A[l] > A[max]:
        max = l
    if r <= size(A) and A[r] > A[max]:
        max = r
    if max != i:
        A[i], A[max] = A[max], A[i]
        heapify_max(A, max)

def build_heap_max(A):

    for i in range(size(A) // 2, 0, -1):
        heapify_max(A, i)


def heapSort(heap):
    build_heap_max(heap)
    size = heap[0]
    for i in range(size,1,-1):
        heap[i], heap[1] = heap[1], heap[i]
        heap[0]-=1
        heapify_max(heap,1)

arr=[9,1,8,4,7,5,6,4,8,0]
heapSort(arr)

def getinmin(heap,x):
    heap[0]+=1
    heap.append((x,0))
    i = size(heap)
    while i > 1 and heap[i][0] > heap[parent(i)][0]:
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent(i)
    return i

def getinmax(heap,x):
    heap[0]+=1
    heap.append((x,0))
    i = size(heap)
    while i > 1 and heap[i][0] < heap[parent(i)][0]:
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent(i)
    return i

class heapMinMax:
    def __init__(self):
        self.heapmax = [0]
        self.heapmin = [0]
    def insert(self, val):
        idxmin = getinmin(self.heapmin, val)
        idxmax = getinmax(self.heapmax, val)
        print(idxmax,idxmin)
        self.heapmin[idxmin] = (self.heapmin[idxmin][0],idxmax)
        self.heapmax[idxmax] = (self.heapmax[idxmax][0],idxmin)

k = heapMinMax()
k.insert(5)
k.insert(6)
print(k.heapmin, k.heapmax)
