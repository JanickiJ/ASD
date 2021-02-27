def findpar(arr, x):
    l = 0
    r = len(arr) - 1
    arr.sort()
    while l < r:
        sum = arr[l] + arr[r]
        if sum == x:
            return True
        elif sum < x:
            l += 1
        else:
            r -= 1
    return False


arr = [6, 9, 11, 1, 3, 7]
print(findpar(arr, 5))
print(arr)
