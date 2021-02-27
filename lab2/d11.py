def diff_between_min_max(arr, k):
    arr.sort()
    min_diff = arr[k]-arr[0]
    mini=0
    for i in range(len(arr)-k):
        diff = arr[i+k]-arr[i]
        if min_diff > diff:
            min_diff = diff
            mini = i
    return mini

arr=[1,36,2,37,5,8,30,40,50,35]
print(diff_between_min_max(arr,3))