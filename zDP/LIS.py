def lis(s):
    n = len(s)
    dp = [1] * n

    for i in range(1,n):
        for j in range(i):
            if s[i] > s[j] and dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
    print(s)
    print(dp)
    return max(dp)

s=[1,7,2,1,4,8,3,10,1]
print(lis(s))