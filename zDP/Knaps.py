def knap(P, W, maxW):
    n = len(W)
    DP = [[0 for _ in range(maxW + 1)] for _ in range(n)]
    Par = [[False for _ in range(maxW + 1)] for _ in range(n)]

    for i in range(W[0], maxW + 1):
        DP[0][i] = P[0]
        Par[0][i] = True

    for i in range(1, n):
        for j in range(1, maxW + 1):
            DP[i][j] = DP[i - 1][j]
            if j >= W[i]:
                if DP[i - 1][j - W[i]] + P[i] > DP[i][j]:
                    DP[i][j] = DP[i - 1][j - W[i]] + P[i]
                    Par[i][j] = True
    result = []

    j = maxW
    i = n-1
    while j > 0:
        if Par[i][j] is True:
            print(i,j)
            result.append(i)
            j -= W[i]
            i-=1
        else:
            i-=1
    print(result)


val = [1, 2, 3]
wt = [1, 2, 3]
W = 5
knap(val,wt,W)

