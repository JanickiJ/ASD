def LCS(set1, set2, n, m, cache):
    if m == 0 or n == 0:
        return 0
    if cache[n][m] != -1:
        return cache[n][m]
    else:
        if set1[n - 1] == set2[m - 1]:
            cache[n][m] = 1+LCS(set1, set2, n - 1, m - 1, cache)
            return cache[n][m]
        else:
            cache[n][m] = max(LCS(set1, set2, n - 1, m, cache), LCS(set1, set2, n, m - 1, cache))
            return cache[n][m]

def LCSmemo(set1, set2):
    n = len(set1)
    m = len(set2)
    cache = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n+1):
        cache[i][0] = 0
    for i in range(m+1):
        cache[0][i] = 0

    LCS(set1, set2, n, m, cache)
    print(cache)
    return cache[n][m]

def LCSiterative(set1,set2):
    n = len(set1)
    m = len(set2)
    cache = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        cache[i][0] = 0
    for i in range(m + 1):
        cache[0][i] = 0

    for i in range(n+1):
        for j in range(m+1):
            if set1[i-1] == set2[j-1]:
                cache[i][j] = 1 + cache[i-1][j-1]
            else:
                cache[i][j] = max(cache[i-1][j],cache[i][j-1])

    result=[None]*cache[n][m]
    printLSC(set1,set2,cache,result)

    print(result)

    return cache[n][m]

def printLSC(set1,set2,cache,result):
    n=len(set1)
    m=len(set2)

    idx=cache[n][m]-1
    j=m
    i=n
    while j>0 and i>0:
        if set1[i-1] == set2[j-1]:
            result[idx] = set1[i-1]
            idx-=1
            j-=1
            i-=1
        else:
            if cache[i-1][j] > cache[i][j-1]:
                i-=1
            else:
                j-=1




a="GXTXAYB"
b="AGGATAB"
print(LCSiterative(a,b))
