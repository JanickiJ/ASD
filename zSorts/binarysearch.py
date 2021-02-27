def binarySearch(arr, x):
    p = 0
    k = len(arr) - 1

    while p <= k:
        mid = (p + k) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            p = mid + 1
        else:
            k = mid - 1
    return -1

arr = [1, 3, 5, 6, 7, 8, 11, 13, 20, 24]
print(binarySearch(arr, 5))

