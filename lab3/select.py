def partition(arr, left, right):
    i = left - 1
    pivot = arr[right]
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def select(tab, p, r, k):
    if p == r:
        return tab[p]
    q = partition(tab, p, r)
    i = q - p + 1
    if k == i:
        return tab[q]
    elif k < i:
        return select(tab, p, q - 1, k)
    else:
        return select(tab, q + 1, r, k - i)


def select1(arr, left, right, k):
    if left == right:
        return arr[left]
    pi = partition(arr, left, right)
    q = pi - left + 1

    if q == k:
        return arr[pi]
    elif k < q:
        return select1(arr, left, pi - 1, k)
    else:
        return select1(arr, pi + 1, right, k - q)


arr = [10, 5, 8, 3, 9, 13, 15, 7, 7, 9, 6, 7, 4, 2, 3, 1, 10]
print(arr)
print(select1(arr, 0, len(arr) - 1, 5))
print(arr)
