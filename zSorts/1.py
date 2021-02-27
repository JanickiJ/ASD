def quicksort(arr, left, right):
    i, j, pivot = left, right, arr[(left + right) // 2]
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j - 1
    if left < j:
        quicksort(arr, left, j)
    if i < right:
        quicksort(arr, i, right)


def sort(arr):
    even = []
    odd = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    quicksort(even, 0, len(even) - 1)
    e, o = 0, 0
    for i in range(len(arr)):
        if e < len(even) and o < len(odd):
            if even[e] > odd[o]:
                arr[i] = odd[o]
                o += 1
            else:
                arr[i] = even[e]
                e += 1

        elif o == len(odd):
            arr[i] = even[e]
            e += 1
        elif e == len(odd):
            arr[i] = odd[o]
            o += 1


arr = [3, 8, 4, 5, 6, 7, 10, 44, 21, 25, 33, 100, 12, 51]
sort(arr)
print(arr)
