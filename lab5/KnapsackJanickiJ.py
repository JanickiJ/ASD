def value(idx):
    return idx[0] / idx[1]

def knapsack(A, k):
    A.sort(key=value)  # sortuje tablice po stosunku wartosci do masy

    n=len(A)
    i = n - 1
    w = 0 #aktualna waga
    p = 0 #aktualny profit
    #napełniam butelke kolejno od najwiekzego st
    #jesli całosc płynu o danym st sie miesci to wlewam cały
    #jeśli nie to wlewam tyle ile sie miesci
    #przy wlewaniu zwiekszam w oraz p

    while i >= 0 and w != k:

        if k - w >= A[i][1]:
            w += A[i][1]
            p += A[i][0]

        else:
            diff = k - w
            p += diff * A[i][0] / A[i][1]
            w += diff

        i -= 1

    return p

# elementarny test, powinien wypisać 12
print(knapsack( [ (1,1), (10,2), (6,3) ], 3 ))
