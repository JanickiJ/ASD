def partition(tab, p, r):
    i = p - 1
    x = tab[r]
    for j in range(p, r):
        if tab[j] < x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def Quicksort(tab):
    stos = [(0, len(tab) - 1)]
    while stos:
        low, high = stos.pop()
        pivot = partition(tab, low, high)
        if low < pivot:
            stos.append((low, pivot - 1))
        if high > pivot:
            stos.append((pivot + 1, high))


def QuickSort(A, i, j):
    size = j - i + 1
    stack = [0] * size
    top = -1

    top += 1
    stack[top] = i
    top += 1
    stack[top] = j

    while top >= 0:
        j = stack[top]
        top -= 1
        i = stack[top]
        top -= 1
        pi = partition(A, i, j)

        if pi - 1 > i:
            top += 1
            stack[top] = i
            top += 1
            stack[top] = pi - 1

        if pi + 1 < j:
            top += 1
            stack[top] = pi + 1
            top += 1
            stack[top] = j


def kthstatistic(tab, low, high, k):
    i = partition(tab, low, high)
    if i == k:
        return tab[i]
    if i < k:
        kthstatistic(tab, low, i - 1, k)
    else:
        kthstatistic(tab, i + 1, high, k)


arr = [9, 5, 1, 8, 2, 7, 3, 6, 45, 33, 44, 55, 61, 54]

print(kthstatistic(arr, 0, len(arr) - 1, 2))
quick_sort(arr)
print(arr)


def SumFromTo(tab, fro, to):
    long = len(tab)
    kthstatistic(tab, 0, long, fro)
    kthstatistic(tab, 0, long, to)
    res = 0
    for i in range(fro, to + 1):
        res += tab[i]
    return res


def Quicksort(A, i, j):
    while i < j:
        q = partition(A, i, j)
        if q - i < j - q:
            QuickSort(A, i, q - 1)
            i = q + 1
        else:
            Quicksort(A, q - 1, j)
            j = q - 1
