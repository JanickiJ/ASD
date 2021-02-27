def subset(sum, set):
    arr = [[False for _ in range(sum + 1)] for _ in range(2)]
    arr[0][0] = True
    print(arr)
    for w in range(1, len(set) + 1):
        for k in range(1, sum+1):
            arr[w % 2][0] = True
            if set[w - 1] > k:
                arr[w % 2][k] = arr[w % 2 + pow(-1,w)][k]
            elif set[w - 1] <= k:
                arr[w % 2][k] = arr[w % 2 + pow(-1,w)][k] or arr[w % 2 + pow(-1,w)][k - set[w - 1]]
    return arr[w % 2][sum]

set = [1,3,1,10,9,11]
print(subset(5,set))

