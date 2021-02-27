from zad2testy import runtests
# korzystam z rekurencji ze spamietywaniem
# tworze tablice zDP która zapisze mi wartosci bezwzglednych wynikow tymczaswych
# tworze tablice par która pomoze mi wybrac z nich minimalny


def opt_sum(tab):
    n = len(tab)
    dp = [[float('inf') for _ in range(n+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = float('inf')
        dp[i][1] = float('inf')
        dp[0][i] = float('inf')

    for i in range(1,n):
        for j in range(2, n+1):
            min = float('inf')
            for t in range(i):
                if min > dp[t][j-1] + abs(tab[t], tab[i]):
                    min = dp[t][j-1]+ abs(tab[t], tab[i])
                dp[i][j] = min
    max = 0
    for i in range(n):
        if max < dp[i][n]:
            max = dp[i][n]
    return max



def abs(a,b):
    s = a+b
    if s > 0:
        return s
    else:
        return s*(-1)

runtests( opt_sum )
