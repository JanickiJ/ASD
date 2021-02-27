def overlap_intervals(arr):
    arr.sort()

    for i in range(len(arr)-1):
        if arr[i][1]>arr[i+1][0]:
            print(arr[i], arr[i+1])


arr=[(1,4),(2,5),(5,6)]
print(arr)
overlap_intervals(arr)
