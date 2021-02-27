def binarySearch(arr, p, k, x):
    if p > k:
        return -1
    mid = (p + k) // 2
    if arr[mid][0] == x:
        return mid
    elif arr[mid][0] > x:
        return binarySearch(arr, p, mid - 1, x)
    else:
        return binarySearch(arr, mid + 1, k, x)


def sort(arr):
    if len(arr) == 0:
        return
    arr1 = [[arr[0],1]]

    for i in range(1,len(arr)):
        x = binarySearch(arr1, 0, len(arr1)-1, arr[i])
        if x != -1:
            arr1[x][1] += 1
        else:
            arr1.append([arr[i], 1])
            i = len(arr1) - 1
            while i > 0 and arr1[i - 1][0] > arr1[i][0]:
                arr1[i - 1], arr1[i] = arr1[i], arr1[i - 1]
                i -= 1
    j=0
    for i in range(len(arr1)):
        while arr1[i][1] != 0:
            arr[j]=arr1[i][0]
            j+=1
            arr1[i][1]-=1

arr=[3,1,5,5,-1,-1,1,1,-5,10,4,5,5]
sort(arr)
print(arr)