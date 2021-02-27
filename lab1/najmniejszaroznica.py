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


def closestNumbers(arr):
    quicksort(arr, 0, len(arr)-1)
    wyniki=[]
    min = abs(arr[1] - arr[0])
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) < min:
            min = abs(arr[i] - arr[i + 1])
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) == min:
            print(arr[i], " ", arr[i + 1], " ")

arr = [-100, -50, -120 , 30, -10, 0, 10, 40, -1000, 70, 50, 80]
print(arr)
quicksort(arr,0 , len(arr)-1)
print(arr)
closestNumbers(arr)
