def zajecia(arr):
    print(arr)
    i=0
    p=i
    counter=1
    results=[]
    results.append(arr[0])
    while i<len(arr):
        if arr[p][1]<=arr[i][0]:
            counter+=1
            p=i
            results.append(arr[i])
        i+=1
    print(results)
    return counter
arr1=[ (0,10), (10,20), (5,15) ]
arr=[(1,2),(0,3),(3,4),(4,5),(0,5),(5,7),(6,8)]
print(zajecia(arr))