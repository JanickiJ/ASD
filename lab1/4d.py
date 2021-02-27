def max_triplet(arr):

    arr.sort()
    max1=arr[len(arr)-1]*arr[len(arr)-2]*arr[len(arr)-3]
    max2=arr[len(arr)-1]*arr[0]*arr[1]
    max_val=max(max1,max2)
    return max_val

