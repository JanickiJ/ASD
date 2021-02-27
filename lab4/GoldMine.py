def goldMine(arr,W,K):
    gold = [[0 for _ in range(len(szachownica))] for _ in range(szachownica)]
    for k in range(K-1,-1,-1):
        for w in range(W):
            up_right = 0
            down_right = 0
            if w != 0:
                up_right = gold[w-1][k+1]
            if w != W-1:
                down_right = gold[w+1][k+1]
            right= gold[w][k+1]
            gold[w][k] = arr[w][k] + max(up_right, down_right, right)

    res = gold[0][0]
    for i in range(W):
       res = max(res, gold[i][0])

    return res


gold = [[1, 3, 1, 5,3],
        [2, 2, 4, 1,2],
        [5, 0, 2, 3,4],
        [0, 6, 1, 2,2]]

m = 4
n = 5

print(goldMine(gold, m, n))