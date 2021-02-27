def partition(arr, start, end):
    i = start - 1
    pivot = arr[end]

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def kthStatistics(arr, start, end, k):
    if start <= end:
        x = partition(arr, start, end)
        if x == k - 1:
            return
        elif x < k - 1:
            kthStatistics(arr, x + 1, end, k)
        else:
            kthStatistics(arr, start, x - 1, k)


def average_score(arr, lowest, highest):
    n = len(arr)
    kthStatistics(arr, 0, n - 1, n - highest + 1)
    kthStatistics(arr, 0, n - 1, lowest)
    sum = 0
    for i in range(lowest - 1, n - highest):
        sum += arr[i]
    print(arr)
    return sum


arr = [1, 4, 87, 3, 9, 4, 6, 7, 8, 5, 3, 5, 4, -5, -2, -88, -2, 66, 44, 24, 66, 4, 0, 0]
print(average_score(arr, 5, 5))
