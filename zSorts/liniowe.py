def countingSort(arr):
    n = len(arr)
    k = max(arr) + 1
    B = [0] * k
    C = [0] * n

    for el in arr:
        B[el] += 1
    for i in range(1, len(B)):
        B[i] += B[i - 1]
    for i in range(n - 1, -1, -1):
        B[arr[i]] -= 1
        C[B[arr[i]]] = arr[i]
    for i in range(n):
        arr[i] = C[i]


def minuscountingSort(arr):
    n = len(arr)
    Min = abs(min(arr))
    Max = max(arr)
    B = [0] * (Min + Max + 1)
    C = [0] * n

    for i in range(n):
        arr[i] += Min
        B[arr[i]] += 1

    for i in range(1, len(B)):
        B[i] += B[i - 1]
    for i in range(n - 1, -1, -1):
        B[arr[i]] -= 1
        C[B[arr[i]]] = arr[i]
    for i in range(n):
        arr[i] = C[i] - Min


def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


def bucketSort(arr):
    n = len(arr)
    norm = max(arr)
    buckets = [[] for _ in range(n+1)]

    for el in arr:
        norm_num = el / norm
        bucket_idx = int(norm_num * n)
        buckets[bucket_idx].append(el)
    for bucket in buckets:
        insertionSort(bucket)

    i = 0
    for bucket in buckets:
        for el in bucket:
            arr[i] = el
            i += 1


def modifiedcountingSort(arr, exp):
    n = len(arr)
    B = [0] * 10
    C = [0] * len(arr)

    for el in arr:
        index = el // exp
        B[index % 10] += 1
    for i in range(1, len(B)):
        B[i] += B[i - 1]
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        B[index % 10] -= 1
        C[B[index % 10]] = arr[i]

    for i in range(len(arr)):
        arr[i] = C[i]


def radixSort(arr):
    maxel = max(arr)
    exp = 1
    while maxel // exp > 0:
        modifiedcountingSort(arr, exp)
        exp *= 10

arr1 = [1,5,6,3,6,8,90,1,11,23,234,46,77,0,0,2,1,3,4]
bucketSort(arr1)
print(arr1)

arr = [111, 432, -12, -40, -54, 81, 7123, -5, 912, 332, 36, -12, -1, -34, 53, 80, 321, 82, 24, 6, 5, 0, 0, 3]
minuscountingSort(arr)
print(arr)
