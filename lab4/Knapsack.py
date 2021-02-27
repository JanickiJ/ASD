def knapsack(P, W, maxWage):
    n = len(P)
    F = [None] * n
    for i in range(maxWage):
        F[i] = [0] * (maxWage + 1)
    for i in range(W[0], maxWage + 1):
        F[0][i] = P[0]
    for i in range(1, n):
        for w in range(1, maxWage + 1):
            F[i][w] = F[i - 1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])
                print(i)
    return F[n - 1][maxWage]

def knapSack(maxW, W, P, n, cache):
    if n == 0 or maxW == 0:
        return 0

    if cache[n - 1][maxW] != -1:
        return cache[n - 1][maxW]

    if W[n - 1] > maxW:
        cache[n - 1][maxW] = knapSack(maxW, W, P, n - 1, cache)
        return cache[n - 1][maxW]
    else:
        cache[n - 1][maxW] = max(P[n - 1] + knapSack(maxW - W[n - 1], W, P, n - 1, cache),knapSack(maxW, W, P, n - 1, cache))
        return cache[n - 1][maxW]

def knapSackRecursive(maxW, W, P, n):
    x = (maxW + 1) * [(-1)]
    cache = (n + 1) * [x]

    return knapSack(maxW, W, P, n, cache)


LCSIteration(s1, s2):
dp = array[length(s1)+1][length(s2)+1]
n = length(s1)
m=length(s2)
for i = 0 to n:
dp[i][m] = 0
for i = 0 to m:
dp[n][i] = 0
for i = n-1 to 0:
for j = m-1 to 0:
if s1[i] == s2[j]:
dp[i][j] = 1+dp[i+1][j+1]
else:
dp[i][j] = MAX(dp[i+1][j], dp[i][j+1])
return dp[0][0]