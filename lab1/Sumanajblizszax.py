def quicksort(arr, left, right):
    i, j, pivot = left, right, arr[(left + right) // 2]
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j - 1
    if left < j:
        quicksort(arr, left, j)
    if i < right:
        quicksort(arr, i, right)


def closest(arr, x):
    s1 = 0
    s2 = len(arr)-1
    mins1=s1
    mins2=s2
    mindiff=abs(x-(arr[s1]+arr[s2]))
    while s2>s1:
        sum=arr[s1]+arr[s2]
        if sum == x:
            return s1,s2
        diff = abs(x - (arr[s1] + arr[s2]))
        if diff<mindiff:
            mins1=s1
            mins2=s2
            mindiff=diff
        if sum<x:
            s1+=1
        else:
            s2-=1
    return mins1,mins2,mindiff

arr = [1, 3,100,13, 5, 7,7,60, 67, 123, 1234, 43, 26]
quicksort(arr,0,len(arr)-1)
print(arr)
print(closest(arr, 40))
