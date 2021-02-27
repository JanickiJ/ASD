def LCS(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 < len2:
        len1, len2 = len2, len1
        s1, s2 = s2, s1

    DP = [[0 for _ in range(len1 + 1)] for _ in range(2)]

    for i in range(1, len1 + 1):
        DP[i % 2][0] = 0
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                DP[i % 2][j] = DP[(i - 1) % 2][j - 1] + 1
            else:
                DP[i % 2][j] = max(DP[i % 2][j - 1], DP[(i - 1) % 2][j])
    print(DP)
    return DP[i % 2][j]


s1 = "AGGTAB"
s2 = "GXTXAYB"
print(LCS(s1, s2))
