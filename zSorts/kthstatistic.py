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
            return arr[x]
        elif x < k - 1:
            return kthStatistics(arr, x + 1, end, k)
        else:
            return kthStatistics(arr, start, x - 1, k)


arr=[0,4,65,8,0,36,23,11,21,12,265,1,1,1111,123,111]
print(kthStatistics(arr,0,len(arr)-1,len(arr)-5))
print(arr)