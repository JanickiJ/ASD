N=100
F = [0] * N
F[0] = 1
F[1] = 1

def FibMem(n):
    if F[n] > 0:
        return F[n]
    F[n] = FibMem(n - 1) + FibMem(n - 2)
    return F[n]

print(FibMem(5))

def LIS(A):
    F=[0]*len(A)
    for i in range(len(A)):
        for j in range(i):
            if A[j]<A[i] and F[j]+1>F[i]:
                F[i]=F[j]+1
    return max(F)