def inversions(arr, left, right, ):
    counter = 0
    if left != right:
        mid = (left + right) // 2
        counter += inversions(arr, left, mid)
        counter += inversions(arr, mid + 1, right)
        counter += merge(arr, left, mid, right)
    return counter


def merge(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    l, r, k = 0, 0, left
    counter = 0
    while l < len(L) and r < len(R):
        if L[l] <= R[r]:
            arr[k] = L[l]
            l += 1
        else:
            arr[k] = R[r]
            r += 1
            counter += mid - l + 1
        k += 1
    while l < len(L):
        arr[k] = L[l]
        l += 1
        k += 1
    while r < len(R):
        arr[k] = R[r]
        r += 1
        k += 1

    return counter


arr = [4,3,1,2]
print(inversions(arr, 0, len(arr) - 1))
