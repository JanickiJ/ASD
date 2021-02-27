import sys


def parent(i):
    return i // 2


def left_son(i):
    return i * 2


def right_son(i):
    return i * 2 + 1


def size(k):
    return k[0]


def heapify(k, i):
    l = left_son(i)
    r = right_son(i)
    maks = i
    if l <= size(k) and k[maks] < k[l]:
        maks = l
    if r <= size(k) and k[maks] < k[r]:
        maks = r
    if maks != i:
        k[i], k[maks] = k[maks], k[i]
        heapify(k, maks)


def build_heap(k):
    for i in range(k[0] // 2, 0, -1):
        heapify(k, i)


def heapSort(k):
    build_heap(k)
    for i in range(size(k), 1, -1):
        k[i], k[1] = k[1], k[i]
        k[0] -= 1
        heapify(k, 1)


def get_max(k):
    if size == 0:
        sys.exit()
    result = k[1]
    k[1] = k[size(k)]
    k[0] -= 1
    heapify(k, 1)
    return result


def insert(k, x):
    if k[0] == len(k) - 1:
        sys.exit()
    k[0] += 1
    k[k[0]] = x
    i = size(k)
    while i > 1 and k[parent(i)] < k[i]:
        k[parent(i)], k[i] = k[i], k[parent(i)]
        i = parent(i)




def sorted_arrays(lists):
    heap_min = [len(lists)]
    n=0
    for i in range(len(lists)):
        heap_min.append(lists[i][0][0])
        n+=len(lists[i])
    result=[]
    build_heap(heap_min)
    while len(result) < n:
        elem, index=heap_min[1]
        lists[index].popleft()

        if lists[index]:
            new_elem=lists[index][0]

arr = [[(1, 1), (4, 1), (7, 1)], [(2, 2), (5, 2), (8, 2)], [(3, 3), (6, 3), (9, 3)]]
sorted_arrays(arr)
arr1=