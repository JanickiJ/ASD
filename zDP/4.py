def sumto(sum,arr):
    n=len(arr)
    cache = [[False for _ in range(sum + 1)] for _ in range(2)]
    cache[0][0]=True

    for w in range(1,n+1):
        cache[w % 2][0] = True
        for k in range(sum+1):
            if arr[w-1] > k:
                cache[w % 2][k] = cache[w%2+ pow(-1,w)][k]
            else:
                cache[w % 2][k] = cache[w%2 + pow(-1,w)][k] or cache[w%2 + pow(-1,w)][k - arr[w-1]]
    return cache[n%2][sum]

set = [1,3,1,10,9,11]
print(sumto(6,set))