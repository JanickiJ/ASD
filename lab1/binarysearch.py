def binarysearch(arr, x):
    p = 0
    k = len(arr)
    while p < k:
        sr = int((p + k) / 2)

        if x == arr[sr]:
            return sr
        elif x > arr[sr]:
            p = sr + 1
        elif x < arr[sr]:
            k = sr
    return -1


def binarysearchreku(arr, p, k, x):
    if p > k:
        return -1
    mid = (p + k) // 2
    if x == arr[mid]:
        return mid
    elif x < arr[mid]:
        return binarysearchreku(arr, p, mid - 1, x)
    else:
        return binarysearchreku(arr, mid + 1, k, x)


def trinary_search(tab, val):
    start = 0
    end = len(tab) - 1
    while start <= end:
        s1=start + (end-start)//3
        s2=start + 2*(end-start)//3
        if tab[s1] == val:
            return s1
        elif tab[s2] == val:
            return s2
        elif tab[s1] > val:
            end=s1-1
        elif tab[s2]<val:
            start=s2+1
        else:
            start=s1+1
            end=s2-1
    return -1


arr = [1, 3, 5, 6, 7, 8, 11, 13, 20, 24]
print(trinary_search(arr, 4))

