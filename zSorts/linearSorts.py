def partition(arr, start, end):
    i = start - 1
    pivot = arr[end]

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quicksort(arr, start, end):
    if start < end:
        q = partition(arr, start, end)
        quicksort(arr, q + 1, end)
        quicksort(arr, start, q - 1)


def merge(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    l, r, k = 0, 0, left
    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            arr[k] = L[l]
            l += 1
        else:
            arr[k] = R[r]
            r += 1
        k += 1
    while l < len(L):
        arr[k] = L[l]
        l += 1
        k += 1
    while r < len(R):
        arr[k] = R[r]
        r += 1
        k += 1


def mergeSort(arr, left, right):
    if right != left:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def right_son(n):
    return 2 * n + 1


def left_son(n):
    return 2 * n


def parent(n):
    return n // 2


def size(heap):
    return heap[0]


def heapify(heap, size, k):
    l = left_son(k)
    r = right_son(k)
    max = k
    if l < size and heap[max] < heap[l]:
        max = l
    if r < size and heap[max] < heap[r]:
        max = r
    if max != k:
        heap[max], heap[k] = heap[k], heap[max]
        heapify(heap, size, max)


def buildheap(arr, size):
    for i in range(size // 2, -1, -1):
        heapify(arr, size, i)


def heapSort(arr):
    size = len(arr)
    buildheap(arr, size)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [1, 4, 7, 9, 2, 6, 3, 8, 3, 8, 4, 6, 5, 0, 0, 3]
mergeSort(arr, 0, len(arr) - 1)
print(arr)
