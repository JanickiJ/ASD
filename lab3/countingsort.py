def countingsort(arr):
    k=max(arr)+1
    B = [0] * len(arr)
    C = [0] * k
    for i in range(len(arr)):
        C[arr[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(len(arr)-1, -1, -1):
        C[arr[i]] -= 1
        B[C[arr[i]]] = arr[i]
    print(B)


arr = [1, 8, 34, 57, 22, 45, 2, 3, 5, 6, 77, 2, 6, 54, 4]
countingsort(arr)

