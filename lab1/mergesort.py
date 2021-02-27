def merge(arr, left, mid, right):
    Left_array=[mid:]
    Right_array=[:mid]
    l,r,m=0
    while l<=mid and r<=right:
        if Left_array[l]<Right_array[r]:
            arr[m]=Left_array[l]
            l+=1
        else:
            arr[m]=Right_array[r]
            r+=1
        m+=1
    while l<=mid:
        arr[m] = Left_array[l]
        l += 1
        m += 1
    while r<=right:
        arr[m] = Right_array[r]
        r += 1
        m += 1


def mergesort(arr, left, right):
    if right != left:
        mid=(left+right)//2
        mergesort(arr, left, mid)
        mergesort(arr, mid +1, right)
        merge(arr, left, mid, right)

arr=[1,3,5,7,9,0,8,6,5,3,2,22,44,7,7,67,34,12,98,9]
print(arr)
mergesort(arr,0,len(arr)-1)
print(arr)