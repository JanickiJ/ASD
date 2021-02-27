# n^2 w dobrych warunkach n
def insort(arr):
    for i in range(len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
A=[1,3,6,9,2,3,4,6,11,14,7]
insort(A)
print(A)