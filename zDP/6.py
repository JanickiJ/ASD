def LIS(arr):
    n=len(arr)
    F=[1]*n
    W=[ [] for _ in range(n)]
    for i in range(n):
        max=-1
        for j in range(i):
            if arr[j] < arr[i] and F[j] + 1 > F[i]:
                max=j
                F[i]=F[j]+1
        for k in range(len(W[max])):
           W[i].append(W[max][k])
        W[i].append(arr[i])
    return (F,W)

def printLIS(F,W):
    max_len=max(F)
    for i in range(len(W)):
        if len(W[i]) == max_len:
            print(W[i])

arr=[1,5,3,100,6,8,93,4,7,15]
F,W = LIS(arr)
printLIS(F,W)
print(max(F))
