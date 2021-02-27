# posortowana tablica podzielona na m kawałkow
# pomieszane i pomieszane w srodku
# złozonosc o(m*nlogn+mlogm)

def sort_unsorted(arr,n):
    m=len(arr)//n
    for i in range(0, m * n, n):
        arr[i:i + n] = sorted(arr[i:i + n])
    arr2 = []
    for i in range(0, m * n, n):
        x = (arr[i], i)
        arr2.append(x)
    arr2.sort()
    curr_idx = 0
    for val, idx in arr2:
        if arr[curr_idx] != val:
            arr[curr_idx:curr_idx + n], arr[idx: idx + n] = arr[idx: idx + n], arr[curr_idx:curr_idx + n]
            curr_idx += n

#posortowanie list posortowanych w 1 liste
#1 pomysł sortujemy dwójkowo n i jest logn takich
