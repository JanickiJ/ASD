def shortest(arr):
    n = len(arr)
    Max = int(max(max(x) for x in arr) * 2 * n)

    DP = [[Max for _ in range(n)] for _ in range(n)]
    DP[0][0] = arr[0][0]

    return reku(n - 1, n - 1, Max, DP, arr)


def reku(i, j, Max, DP, arr):

    if DP[i][j] < Max:
        return DP[i][j]
    elif i == 0:
        DP[i][j] = reku(i, j - 1, Max, DP, arr) + arr[i][j]
    elif j == 0:
        DP[i][j] = reku(i - 1, j, Max, DP, arr) + arr[i][j]
    else:
        DP[i][j] = min(reku(i, j - 1, Max, DP, arr), reku(i - 1, j, Max, DP, arr)) + arr[i][j]
    return DP[i][j]

arr = [
    [1, 1, 2],
    [2, 1, 1],
    [2, 2, 1]
]

print(shortest(arr))
