def tasks(A):
    #tworze nowa tablice która składa sie z krotek odwróconych, czyli (ei,bi)
    B=[]
    for i in range(len(A)):
        B.append((A[i][1],A[i][0]))
    #Sortuje B po czasie zakonczenia sie zajec
    B.sort()
    #Rozpoczynam zliczanie
    i = 0
    p = i  # p oznacza poprzedni przedział
    counter = 1

    while i < len(B):

        if B[p][0]<=B[i][1]:
            counter+=1
            p=i     #teraz i bedzie moim poprzednim przediałem

        i+=1

    return counter

# elementarny test, powinien wypisać 2
print( tasks([ (0,10), (10,20), (5,15) ] ))
