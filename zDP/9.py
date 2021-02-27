def coins(arr,sum):
    sums=[float('inf')]*(1+sum)
    sums[0] = 0
    for i in range(sum+1):
        for j in arr:
            if i-j >=0 and sums[i-j]+1<sums[i]:
                sums[i] = sums[i-j]+1
    return sums

arr=[1,5,8]
print(coins(arr,15))