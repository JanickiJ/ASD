def insertsort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def bucketsort(arr, n):
    norm = max(arr)
    buckets = [[] for i in range(n)]

    for num in arr:
        norm_num = num / norm
        bucket_idx = int(n * norm_num)
        buckets[bucket_idx].append(num)
    for i in range(n):
        insertsort(buckets[i])
    output = []
    for i in range(n):
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])
    for i in range(len(arr)):
        arr[i] = output[i]


arr = [1, 5, 7, 10, 99, 45, 76, 3, 2, 67, 87, 23, 23, 7, 7, 3]
bucketsort(arr, 100)
print(arr)
