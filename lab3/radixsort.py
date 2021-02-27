def countingsort(arr, exp):
    b = [0] * len(arr)
    c = [0] * 10

    for i in range(len(arr)):
        index=arr[i]//exp
        c[index % 10] += 1
    for i in range(1, len(c)):
        c[i] += c[i - 1]
    for i in range(len(arr)-1, -1, -1):
        index = arr[i] // exp
        c[index % 10] -= 1
        b[c[index % 10]] = arr[i]
    for i in range(len(arr)):
        arr[i] = b[i]


def radixsort(arr):
    maxel = max(arr)
    exp = 1
    while maxel // exp > 0:
        countingsort(arr, exp)
        exp *= 10

arr=[9999,9123,9876,9545,9664,9534,7423,9654,9664,1234,9123,74,832,74]
print(arr)
radixsort(arr)
print(arr)