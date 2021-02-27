def chessmoving(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if j>0 and i>0:
                mindis=min(arr[i][j-1],arr[i-1][j])
            elif i == 0:
                mindis = arr[i][j-1]
            elif j == 0:
                mindis = arr[i-1][j]
            if i !=0 or j!= 0:
                arr[i][j] +=mindis
    print(arr)
    return arr[n-1][n-1]

arr=[[1,1,1],[4,7,1],[1,1,1]]
print(chessmoving(arr))