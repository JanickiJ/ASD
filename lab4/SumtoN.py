
def sumreku(arr,n,counter):
    if n < 0:
        return counter
    elif n == 0:
        return counter+1
    else:
        for i in range(len(arr)):
            return sumreku(arr,n-arr[i],counter)
    return counter



def sumbottomup(arr,N):
    m=len(arr)
    helper = [0]*(N+1)
    helper[0]=1
    for i in range(1 , N+1):
        for j in arr:
            if i>=j:
                helper[i]+=helper[i-j]
    return helper[N]


arr = [1,5,6]
print(sumbottomup(arr,7))