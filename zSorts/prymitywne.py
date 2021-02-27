def bubbleSort(arr):
    n = len(arr)
    change = True
    i = 0
    while i < n - 1 and change:
        change = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                change = True
        i += 1


def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

arr = [1, 7, 3, 9, 0, 0, 0, 7, 6, 5, 4, 5, 6, 7, 13, 0, 3, 1]
print(arr)
insertionSort(arr)
print(arr)
