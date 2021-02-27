def coins(arr, sum):
    n=len(arr)
    DP=[[float('inf') for _ in range(sum+1)]for _ in range(n)]
    j = arr[0]
    c=1

    for j in range(arr[0],sum+1,arr[0]):
        DP[0][j] = c
        c+=1
    for i in range(n):
        DP[i][0] = 0

    for i in range(1,n):
        for j in range(1,sum+1):
            DP[i][j] = DP[i-1][j]
            if j >= arr[i]:
                DP[i][j] = min(DP[i][j-arr[i]]+1, DP[i][j])
    print(DP)
    return DP[n-1][sum]

arr=[3,5]
print(coins(arr,7))

