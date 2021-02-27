def floyd_warshall(G):
    n=len(G)
    S=[[ float('inf') for _ in range (n) ] for _ in range (n)]

    for i in range (n):
        S[i][i]=0

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                S[i][j] = G[i][j]

    for t in range(n):
        for i in range(n):
            for j in range(n):
                S[i][j]=min(S[i][j],S[i][t]+S[t][j])
    return(S)