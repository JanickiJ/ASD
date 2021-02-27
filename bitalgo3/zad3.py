def insertsort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def bucketsort(arr):
    norm = max(arr)
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        norm_num = num / norm
        index = int(norm_num * n)
        buckets[index].append(num)

    flag=True
    for i in range(n):
        if(len(buckets[i]))> (n+1)/2:
            large_bucket=i
    if flag == True:
        insertsort(arr)
