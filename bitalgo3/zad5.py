def insersort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def sort(arr, k, x):
    B = [0] * (k + 1)
    C = [0] * (len(arr) - x)
    smaller = []
    bigger = []
    for num in arr:
        if num > k:
            bigger.append(num)
        elif num < 0:
            smaller.append(num)
        else:
            B[num] += 1
    insersort(smaller)
    insersort(bigger)
    for i in range(1, k + 1):
        B[i] += B[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        if 0 < arr[i] <= k:
            B[arr[i]] -= 1
            C[B[arr[i]]] = arr[i]

    i = 0
    j = 0
    while i < len(smaller):
        arr[j] = smaller[i]
        j += 1
        i += 1
    i = 0
    while i < len(C):
        arr[j] = C[i]
        i += 1
        j += 1
    i = 0
    while i < len(bigger):
        arr[j] = bigger[i]
        j += 1
        i += 1


arr = [60, 63, 61, 70, 65, 60, 30, 20, 10, 50, 15, 33, 21, -5, -10, -7, -3]
sort(arr, 50, 10)
print(arr)
