#rozwiazanie analogiczne do rozwiazaia problemu knapsack(bez 2 wymiaru) z wykładu,
# róznica jest taka ze operujemy na tablicy 3 wymiarowej
def knapsack2d(P, max_w, max_h):
    n = len(P)
    #tworze tablice 3 wymiarowa
    # 1 wymiar to numer przedmiotu i
    # 2 wymiar to waga przedmiotu w
    # 3 wymiar to wysokosc przedmiotu h
    F= [None] * n
    for i in range(n):
        F[i] = [0] * (max_w + 1)
        for w in range(max_w+1):
            F[i][w] = [0] * (max_h + 1)
    #wypełniam tablice wartosciami poczatkowymi
    #czyli jesli przedmiot 1 sie miesci to dodaje profit do odpowienich pol
    for w in range(P[0][1],max_w+1):
        for h in range(P[0][2], max_h+1):
            F[0][w][h] = P[0][0]
    #wypełniam cała tablice
    #jesli i-ty przedmiot aktualnie miesci sie to go biore lub nie zaleznie od tego co jest korzystniejsze
    for i in range(1, n):
        for w in range(1, max_w + 1):
            for h in range(1, max_h +1):
                F[i][w][h] = F[i-1][w][h]
                if w >= P[i][1] and h >= P[i][2]:
                    F[i][w][h] = max(F[i][w][h], F[i - 1][w - P[i][1]][h - P[i][2]] + P[i][0])
    #najwiekszym profitem bedzie ,,ostatnia'' komorka tablicy
    return F[n-1][max_w][max_h]

P = [(5, 10, 3), (7, 8, 12), (2, 7, 3)]
print(knapsack2d(P, 16, 15))  # wypisze 9

