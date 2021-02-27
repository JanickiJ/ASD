def findDistinc(arr):
    l = 0
    r = len(arr) - 1
    counter = 0
    while l < r:

        if arr[l] == arr[l + 1]:
            l += 1
        elif arr[r] == arr[r - 1]:
            r -= 1
        elif arr[l] + arr[r] == 0:
            counter += 1
            l += 1
        elif arr[l] + arr[r] < 0:
            l += 1
        elif arr[l] + arr[r] > 0:
            r -= 1

    if arr[l] + arr[r] == 0:
        counter += 1
    return counter


arr = [-3, -2, -2, -2, -1, 1, 2, 2, 2, 3]
print(findDistinc(arr))
