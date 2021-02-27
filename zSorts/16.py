def doublecounting(arr,exp):
    n=len(arr)
    B=[0]*n
    C=[0]*n

    for el in arr:
        idx = el // exp
        B[idx % n] += 1
    for i in range(1, len(B)):
        B[i] += B[i - 1]
    for i in range(n - 1, -1, -1):
        idx = arr[i] // exp
        B[idx % n] -= 1
        C[B[idx % n]] = arr[i]
    for i in range(n):
        arr[i] = C[i]

def radix(arr):
    doublecounting(arr,1)
    doublecounting(arr,len(arr))

arr=[0,5,5,90,99]
radix(arr)
print(arr)
