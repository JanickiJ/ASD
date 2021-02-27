def partition(arr, left, right):
    i = left - 1
    pivot = arr[right]

    for j in range(left , right):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[right], arr[i + 1] = arr[i + 1], arr[right]
    return (i + 1)


def quick_sort(arr, left, right):
    if left < right:
        i = partition(arr, left, right)
        quick_sort(arr, left, i - 1)
        quick_sort(arr, i + 1, right)


tablica = [4, 17, 6, 91, 56, 4, 4, 4, 4, 23, 9, 100, 75, 4, 7, 42, 85, 10]
print(tablica)
quick_sort(tablica, 0, len(tablica) - 1)
print(tablica)
