def uglynumbers(n):
    arr = [0]*n
    arr[0] = 1
    idx_2,idx_3,idx_5=0,0,0
    next_of_2 = 2
    next_of_3 = 3
    next_of_5 = 5
    for i in range(1,n):
        arr[i]= min(next_of_2,next_of_3,next_of_5)
        if arr[i] == next_of_2:
            idx_2 += 1
            next_of_2 = 2 * arr[idx_2]
        if arr[i] == next_of_3:
            idx_3 += 1
            next_of_3 = 3 * arr[idx_3]

        if arr[i] == next_of_5:
            idx_5 += 1
            next_of_5 = 5 * arr[idx_5]

    return arr
print(uglynumbers(10))