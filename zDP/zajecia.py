def zajecia(arr, k):
    n = len(arr)
    arr = sorted(arr, key=lambda item: item[1])
    dp = [[float('inf') for _ in range(k+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0
        dp[i][1] = 0

    for i in range(1, n):
        for j in range(2, k + 1):
            for m in range(i):
                dis = arr[i][0] - arr[m][1]
                if dis > 0 and dp[m][j-1] + dis < dp[i][j]:
                    dp[i][j] = dp[m][j-1] + dis

    result = float('inf')
    for i in range(n):
        if result > dp[i][k]:
            result = dp[i][k]

    print(result)


arr = [(4,6), (2,7), (3,10),(1,5),(2,6),(8,10)]
zajecia(arr)
