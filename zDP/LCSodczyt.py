def Lcs(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 < len2:
        len1,len2= len2, len1
        s1,s2=s2,s1

    DP = [[0 for _ in range(len1+1)] for _ in range(len2+1)]

    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if s1[i-1] == s2[j-1]:
                DP[i][j] = DP[i - 1][j - 1] + 1
            else:
                DP[i][j] = max(DP[i][j - 1], DP[i][j])
    LCS=[]
    i=len1
    j=len2
    while i!= 0 and j!=0:
        if DP[i-1][j-1]+1 == DP[i][j]:
            LCS.append(s1[i-1])
            i-=1
            j-=1
        elif DP[i-1][j] >= DP[i][j-1]:
            i-=1
        elif DP[i-1][j] < DP[i][j-1]:
            j-=1

    print(LCS)

s1 = "AGGTAB"
s2 = "GXTXAB"
print(Lcs(s1, s2))
