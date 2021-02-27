def cathalannumber(n):
    cath=[0]*(n+1)
    cath[0] = 1

    for i in range(0, n):
        for j in range(i+1):
            cath[i+1] += cath[j]*cath[i-j]
    return cath

print(cathalannumber(3))