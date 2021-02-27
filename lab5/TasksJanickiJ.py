def tasks(A):
    #sortuje po ei
    A.sort(key = lambda x: x[1])

    #Rozpoczynam zliczanie
    i = 0
    p = i  # p oznacza poprzedni przedział
    counter = 1

    while i < len(A):

        if A[p][1]<=A[i][0]:
            counter+=1
            p=i     #teraz i bedzie moim poprzednim przedziałem

        i+=1

    return counter

# elementarny test, powinien wypisać 2
print( tasks([ (0,10), (10,20), (5,15) ] ))
